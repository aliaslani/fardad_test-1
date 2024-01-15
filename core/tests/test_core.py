import pytest
from django.contrib.auth.models import User
from model_bakery import baker
from rest_framework import status
from core.models import Log
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


@pytest.mark.django_db
class TestTokenApi:

    # def test_bad_input_data_returns_400(self, api_client):
    #     response = api_client.post("/core/get_token/", {"username": "admin", "password": ""})
    #     assert response.status_code == status.HTTP_400_BAD_REQUEST

    # def test_get_token_correctly_returns_200(self, api_client):
    #     user = baker.make(User)
    #     response = api_client.post("/core/get_token/", {"username": user.username, "password": user.password})
    #     assert response.status_code == status.HTTP_200_OK
    
    def test_custom_auth_token(self, api_client):
            # Create a test user
            test_user = User.objects.create_user(username='testuser', password='testpassword')

            # Simulate a POST request to obtain a custom auth token
            response = api_client.post('/core/get_token/', {'username': 'testuser', 'password': 'testpassword'}, format='json')

            # Check if the request was successful (status code 200)
            assert response.status_code == status.HTTP_200_OK

            # Check if the response contains a 'token' key
            assert 'token' in response.data

            # Check if a new Token was created for the user
            token = Token.objects.get(user=test_user)
            assert response.data['token'] == token.key