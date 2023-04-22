# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

# Internal
from .models import Watch
from tasks.models import Task
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class WatchViewTests(APITestCase):
    def setUp(self):
        """
        Automatically runs before every test method
        """
        User.objects.create_user(username='api_test_user_1', password='password123')

    def test_not_logged_in_user_cannot_watch_task(self):
        """
        Test to ensure unauth user cannot watch task
        """
        response = self.client.post('/watches/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class WatchDetailViewTests(APITestCase):
    def setUp(self):
        """
        Contains two users, 3 tasks and 2 watches
        """
        api_test_user_1 = User.objects.create_user(username='api_test_user_1', password='password123')
        api_test_user_2 = User.objects.create_user(username='api_test_user_2', password='password123')
        Task.objects.create(
            owner=api_test_user_1, title='task title',
            task_body='test'
        )
        Task.objects.create(
            owner=api_test_user_1, title='Task title 2',
            task_body='test2'
        )
        Task.objects.create(
            owner=api_test_user_2, title='Task title 3',
            task_body='test3'
        )
        Watch.objects.create(owner=api_test_user_1, task_id=1)
        Watch.objects.create(owner=api_test_user_2, task_id=2)

    def test_auth_user_can_watch_task(self):
        """
        Test to ensure logged-in user can create a watch
        """
        self.client.login(username='api_test_user_1', password='password123')
        response = self.client.post('/watches/', {'task': 3})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_can_retrieve_existing_watch(self):
        """
        Test if possible to retrieve a watch by its ID
        """
        self.client.login(username='api_test_user_1', password='password123')
        response = self.client.get('/watches/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_retrieve_non_existing_watch(self):
        """
        Test if possible to retrieve a watch with no ID
        """
        self.client.login(username='api_test_user_1', password='password123')
        response = self.client.get('/watches/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_unwatch_owned_watch(self):
        """
        Test if user can remove watch (unwatch a task)
        """
        self.client.login(username='api_test_user_1', password='password123')
        response = self.client.delete('/watches/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_can_unwatch_other_user_watched(self):
        """
        Test if user can remove someone else's watch
        (unwatch a task for someone)
        """
        self.client.login(username='api_test_user_1', password='password123')
        response = self.client.delete('/watches/2/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def tearDown(self):
        """
        Automatically runs after every test method
        """
        Watch.objects.all().delete()
        Task.objects.all().delete()
        User.objects.all().delete()
