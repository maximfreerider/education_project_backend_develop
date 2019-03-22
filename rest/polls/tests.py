from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status


class AccountsTest(APITestCase):
    def SetUp(self):
        self.test_user = User.objects.create_user('testuser',
                                                  'test@example.com',
                                                  'testpass')

        self.create_url = reverse('account-create')

    def test_create_user(self):
        data = {
            'username': 'foobar',
            'email': 'foobar@example.com',
            'password': 'somepassword'
        }

        responce = self.client.post(self.create_url, data, format='json')

        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(responce.status_code, status.HTTP_201_CREATED)
        self.assertEqual(responce.data['username'], data['username'])
        self.assertEqual(responce.data['email'], data['email'])
        self.assertFalse('password' in responce.data)
 