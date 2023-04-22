# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

# Internal
from .models import Pack
from tasks.models import Task
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class PackViewTests(APITestCase):
    def setUp(self):
        """
        Automatically runs before every test method
        """
        User.objects.create_user(
            username='api_test_user_1', password='password123')

    def test_unauth_user_cannot_view_packs(self):
        """
        Test to ensure not logged-in user cannot view packs
        """
        response = self.client.post('/packs/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PackDetailViewTests(APITestCase):
    def setUp(self):
        """
        Contains 3 tasks and 2 packs and 2 users
        """
        api_test_user_1 = User.objects.create_user(
            username='api_test_user_1', password='password123')
        api_test_user_2 = User.objects.create_user(
            username='api_test_user_2', password='password123')

        task_1 = Task.objects.create(
            owner=api_test_user_1, title='task title 1',
            task_body='testing 1'
        )

        task_2 = Task.objects.create(
            owner=api_test_user_1, title='task title 2',
            task_body='testing 2'
        )

        task_3 = Task.objects.create(
            owner=api_test_user_1, title='task title 3',
            task_body='testing 3'
        )

        pack_1 = Pack.objects.create(owner=api_test_user_1, title='title 1')
        pack_1.tasks.add(task_1, task_2)

        pack_2 = Pack.objects.create(owner=api_test_user_2, title='title 2')
        pack_2.tasks.add(task_3)

    def test_auth_user_can_create_pack(self):
        """
        Test to ensure logged-in user can create a pack
        """
        self.client.login(username='api_test_user_1', password='password123')
        response = self.client.post('/packs/', {'title': 'My Pack', 'tasks': 1})
        print(response.status_code)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_can_retrieve_existing_pack(self):
        """
        Test if possible to retrieve a pack by its ID
        """
        self.client.login(username='api_test_user_1', password='password123')
        response = self.client.get('/packs/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_retrieve_non_existing_pack(self):
        """
        Test if possible to retrieve a following with no ID
        """
        self.client.login(username='api_test_user_1', password='password123')
        response = self.client.get('/packs/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_delete_owned_pack(self):
        """
        Test if user can unfollow user
        """
        self.client.login(username='api_test_user_1', password='password123')
        response = self.client.delete('/packs/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_can_delete_other_user_pack(self):
        """
        Test if user can delete other user's pack
        """
        self.client.login(username='api_test_user_1', password='password123')
        response = self.client.delete('/pack/2/')
        print(response.status_code)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
