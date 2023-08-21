from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class RegistrationTestCase(TestCase):
    def test_registration(self):
        response = self.client.post(reverse('register'), {
            'username': 'testuser',
            'password': 'testpass123'
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.count(), 1)
