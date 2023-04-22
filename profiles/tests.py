# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

# Internal
from .models import Profile
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class ProfileDetailViewTests(APITestCase):
    def setUp(self):
        """
        Creates two users
        Associated profile for each user is automatically created
        using Django signals
        """
        User.objects.create_user(username='api_test_user_1',
                                 password='password123')
        User.objects.create_user(username='api_test_user_2',
                                 password='password123')

    def test_user_can_view_existing_profile(self):
        """
        Test to view existing profile
        """
        self.client.login(username='api_test_user_1', password='password123')
        response = self.client.get('/profiles/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_view_non_existing_profile(self):
        """
        Test to view a profile which doesn't exist
        """
        self.client.login(username='api_test_user_1', password='password123')
        response = self.client.get('/profiles/9999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_owned_profile(self):
        """
        Test user can update a profile they own
        """
        self.client.login(username='api_test_user_1', password='password123')
        response = self.client.put('/profiles/1/',
                                   {'name': 'john'})
        profile = Profile.objects.filter(pk=1).first()
        self.assertEqual(profile.name, 'john')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_update_other_profiles(self):
        """
        Test user cannot update other users' profiles
        """
        self.client.login(username='api_test_user_1', password='password123')
        response = self.client.put('/profiles/2/', {'name': 'mary'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_un_auth_user_can_update_owned_profile(self):
        """
        Test user can update their profile when not logged in
        """
        response = self.client.put('/profiles/1/',
                                   {'name': 'john'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_delete_owned_profile(self):
        """
        Test user can delete their own profile
        """
        self.client.login(username='api_test_user_1', password='password123')
        response = self.client.delete('/profiles/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def tearDown(self):
        """
        Automatically runs after every test method
        """
        Profile.objects.all().delete()
        User.objects.all().delete()
