# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

# Internal
from .models import Contact
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class ContactViewTests(APITestCase):
    def setUp(self):
        """
        Automatically runs before every test method
        """
        User.objects.create_user(
            username='api_test_user_1', password='password123')

    def test_non_auth_user_can_post_contact(self):
        """
        Test to ensure non auth user can send a contact form
        """
        response = self.client.post('/contact/', {
            'reason': 'GENERAL',
            'name': 'tester',
            'email': 'test@task.com',
            'message': 'test contact form'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_auth_user_can_post_contact(self):
        """
        Test to ensure auth user can send a contact form
        """
        self.client.login(username='api_test_user_1', password='password123')
        response = self.client.post('/contact/', {
            'name': 'tester',
            'email': 'test@task.com',
            'message': 'test contact form'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_task_includes_all_required_fields(self):
        """
        Test to verify if contact form can be posted
        without filling in mandatory fields (name, email, message)
        """
        self.client.login(username='api_test_user_1', password='password123')
        response = self.client.post(
            '/contact/', {'message': 'Missing required fields'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def tearDown(self):
        """
        Automatically runs after every test method
        """
        Contact.objects.all().delete()
        User.objects.all().delete()
