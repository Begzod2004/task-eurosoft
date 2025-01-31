from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status

class TextApiTests(APITestCase):
    def test_convert_text(self):
        response = self.client.post('/api/convert/', {'text': 'salom dunyo'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['result'], 'салом дунё')

    def test_calculate_days(self):
        response = self.client.post('/api/calculate-days/', {'birth_date': '1990-01-01'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('days' in response.data)
