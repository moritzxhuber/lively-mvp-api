# from unittest.mock import patch

from django.test import TestCase
from django.contrib.auth import get_user_model

# from core import models


def sample_user(username='testuser', email='test@gmail.com',
                password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(username, email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        username = 'moritzhuber'
        email = 'moritz.mh.huber@gmail.com'
        password = 'ourpassion'
        user = get_user_model().objects.create_user(
            username=username,
            email=email,
            password=password
        )

        self.assertEqual(user.username, username)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'moritz.mh.huber@GMAIL.COM'
        user = get_user_model().objects.create_user('moritzhuber', email,
                                                    'ourpassion')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_username(self):
        """Test creating user with no username raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,
                                                 'moritz.mh.huber@gmail.com',
                                                 'ourpassion')

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('moritzhuber', None,
                                                 'ourpassion')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'moritzhuber',
            'moritz.mh.huber@gmail.com',
            'ourpassion'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
