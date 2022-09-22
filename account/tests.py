from django.urls import reverse
from rest_framework import status
from django.test import TestCase




class CreateAccount(TestCase):

    def test_create_account(self):
        url = reverse("create_account")
        data = {"name":"cisco quan","password":"Wowme2023", "email":"me@data2bot.com"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)




