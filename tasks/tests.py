# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

# Internal
from .models import Task
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TaskViewTests(APITestCase):
    def setUp(self):
        """
        Automatically runs before every test method
        """
        User.objects.create_user(
            username='api_test_user_1', password='password123')

    def test_non_auth_user_cannot_create_task(self):
        """
        Test to ensure non auth user cannot create a task
        """
        response = self.client.post('/tasks/', {'title': 'test task'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_auth_user_can_create_task(self):
        """
        Test to ensure auth user can create a task
        """
        self.client.login(username='api_test_user_1', password='password123')
        response = self.client.post(
            '/tasks/', {'title': 'task title', 'task_body': 'task 1 body'})
        task_count = Task.objects.count()
        self.assertEqual(task_count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_task_includes_all_required_fields(self):
        """
        Test to verify if task can be created
        without filling in mandatory fields (task title & task body)
        """
        self.client.login(username='api_test_user_1', password='password123')
        response = self.client.post('/tasks/', {'task_body': 'Missing title'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_can_list_tasks(self):
        """
        Test that tasks present in the database can be listed
        """
        api_test_user_1 = User.objects.get(username='api_test_user_1')
        Task.objects.create(owner=api_test_user_1, title='task title')
        response = self.client.get('/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TaskDetailViewTests(APITestCase):
    def setUp(self):
        """
        Contains two users with a task created by each user
        """
        api_test_user_1 = User.objects.create_user(
            username='api_test_user_1', password='password123')
        api_test_user_2 = User.objects.create_user(
            username='api_test_user_2', password='password123')
        Task.objects.create(
            owner=api_test_user_1, title='task title 1',
            task_body='test task 1'
        )
        Task.objects.create(
            owner=api_test_user_2, title='task title 2',
            task_body='test task 2'
        )

    def test_can_retrieve_existing_task(self):
        """
        Test if possible to retrieve a task which exists
        """
        response = self.client.get('/tasks/1/')
        self.assertEqual(response.data['title'], 'task title 1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cannot_retrieve_non_existing_task(self):
        """
        Test if possible to retrieve a task which does not exist
        """
        response = self.client.get('/tasks/9999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_owned_task(self):
        """
        Test if user can update a task they own
        """
        self.client.login(username='api_test_user_1', password='password123')
        response = self.client.put(
            '/tasks/1/', {'title': 'updated title 1',
                          'task_body': 'task 1 body'})
        task = Task.objects.filter(pk=1).first()
        self.assertEqual(task.title, 'updated title 1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_update_other_users_task(self):
        """
        Test if user can update other users' tasks
        """
        self.client.login(username='api_test_user_1', password='password123')
        response = self.client.put('/tasks/2/', {'title': 'updated title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_delete_their_own_task(self):
        """
        Test if user can delete their task
        """
        self.client.login(username='api_test_user_1', password='password123')
        response = self.client.delete('/tasks/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_cannot_delete_other_users_task(self):
        """
        Test if user can delete other users' tasks
        """
        self.client.login(username='api_test_user_1', password='password123')
        response = self.client.delete('/tasks/2/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def tearDown(self):
        """
        Automatically runs after every test method
        """
        Task.objects.all().delete()
        User.objects.all().delete()
