# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

# Internal
from .models import Comment
from tasks.models import Task
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class CommentTests(APITestCase):
    def setUp(self):
        """
        Automatically runs before every test method
        """
        User.objects.create_user(
            username='api_test_user', password='password123')

    def test_unauth_user_cannot_create_comment(self):
        """
        Test to ensure not logged-in user cannot create a comment
        """
        response = self.client.post('/comments/', {'content': 'test comment'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class CommentDetailViewTests(APITestCase):
    def setUp(self):
        """
        Contains two users with task and comments for each
        """
        api_test_user = User.objects.create_user(
            username='api_test_user', password='password123')
        api_test_user_2 = User.objects.create_user(
            username='api_test_user_2', password='password123')
        Task.objects.create(
            owner=api_test_user, title='task title',
            task_body='test'
        )
        Task.objects.create(
            owner=api_test_user_2, title='Task title 2',
            task_body='test2'
        )
        Comment.objects.create(owner=api_test_user, task_id=1,
                               comment_body='api_test_user comment1')
        Comment.objects.create(owner=api_test_user_2, task_id=2,
                               comment_body='api_test_user_2 comment2')

    def test_auth_user_can_create_comment(self):
        """
        Test to ensure logged-in user can create a comment
        """
        self.client.login(username='api_test_user', password='password123')
        response = self.client.post('/comments/', {'task': 1,
                                                   'comment_body': 'a test comment'})
        comment_count = Comment.objects.count()
        self.assertEqual(comment_count, 3)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_comment(self):
        """
        Test if possible to retrieve a comment which exists
        """
        self.client.login(username='api_test_user', password='password123')
        response = self.client.get('/comments/1/')
        self.assertEqual(
            response.data['comment_body'], 'api_test_user comment1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_non_existing_comment(self):
        """
        Test if possible to retrieve a comment which does not exist
        """
        self.client.login(username='api_test_user', password='password123')
        response = self.client.get('/comments/9999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_owned_comment(self):
        """
        Test if user can update a comment they created
        """
        self.client.login(username='api_test_user', password='password123')
        response = self.client.put('/comments/1/',
                                   {'comment_body': 'updated comment'})
        comment = Comment.objects.filter(pk=1).first()
        self.assertEqual(comment.comment_body, 'updated comment')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_update_non_owned_comment(self):
        """
        Test if user can update other users' comment
        """
        self.client.login(username='api_test_user', password='password123')
        response = self.client.put('/comments/2/',
                                   {'comment_body': 'updated comment'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_delete_owned_comment(self):
        """
        Test if user can delete their own comment
        """
        self.client.login(username='api_test_user', password='password123')
        response = self.client.delete('/comments/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_cannot_delete_non_owned_comment(self):
        """
        Test if user can delete other users' comment
        """
        self.client.login(username='api_test_user', password='password')
        response = self.client.delete('/comments/2/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def tearDown(self):
        """
        Automatically runs after every test method
        """
        Comment.objects.all().delete()
        Task.objects.all().delete()
        User.objects.all().delete()
