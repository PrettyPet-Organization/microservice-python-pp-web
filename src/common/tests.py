from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class RandomTimeViewTests(APITestCase):

    def test_random_time_view(self):
        response = self.client.get(reverse("random_time"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that the response contains the expected keys
        self.assertIn("country", response.data)
        self.assertIn("time", response.data)
