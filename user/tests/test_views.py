import pytest
from rest_framework.reverse import reverse
from rest_framework import status

pytestmark = pytest.mark.django_db


# Create your tests here.


class TestUserRegistrationAPIView:
    payload = {
        "email": 'test@mail.com',
        "user_type": "Admin",
        "password": "admin@123",
        "password2": "admin@123"
    }

    def test_register_new_user(self, client):
        payload = self.payload
        url = reverse("user:register")
        get_response = client.post(url, data=payload, format='json')
        assert get_response.status_code == status.HTTP_201_CREATED

    def test_register_new_user_with_existing_email(self, client):
        payload = self.payload
        url = reverse("user:register")
        get_response = client.post(url, data=payload, format='json')
        assert get_response.status_code == status.HTTP_201_CREATED

        get_response = client.post(url, data=payload, format='json')
        assert get_response.status_code == status.HTTP_400_BAD_REQUEST
        assert get_response.json() is not None

    def test_register_new_user_with_non_matching_password(self, client):
        payload = {
            "email": 'test@mail.com',
            "user_type": "Admin",
            "password": "admin@123",
            "password2": "admin@1234"
        }
        url = reverse("user:register")
        get_response = client.post(url, data=payload, format='json')
        assert get_response.status_code == status.HTTP_400_BAD_REQUEST
        assert get_response.json() is not None

    def test_register_new_user_with_no_payload(self, client):
        url = reverse("user:register")
        get_response = client.post(url, format='json')
        assert get_response.status_code == status.HTTP_400_BAD_REQUEST
        assert get_response.json() is not None

    def test_not_allowed_method_does_not_work_in_registration_api(self, auth_client):
        url = reverse("user:register")
        get_response = auth_client.get(url)
        assert get_response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        assert get_response.json() is not None

        put_response = auth_client.put(url)
        assert put_response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        assert put_response.json() is not None

        patch_response = auth_client.patch(url)
        assert patch_response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        assert patch_response.json() is not None

        delete_response = auth_client.delete(url)
        assert delete_response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        assert delete_response.json() is not None


class TestLoginAPIView:
    def test_login_valid_user(self, auth_client):
        payload = {
            "email": "new@mail.com",
            "user_type": "Admin",
            "password": "admin@123",
            "password2": "admin@123"
        }
        url = reverse("user:register")
        get_response = auth_client.post(url, data=payload, format='json')
        assert get_response.status_code == status.HTTP_201_CREATED

        payload = {
            "email": "new@mail.com",
            "password": "admin@123"
        }
        url = reverse("user:login")
        get_response = auth_client.post(url, data=payload, format='json')
        assert get_response.status_code == status.HTTP_200_OK

    def test_login_invalid_user(self, auth_client):
        payload = {
            "email": "new@mail.com",
            "password": "admin@123"
        }
        url = reverse("user:login")
        get_response = auth_client.post(url, data=payload, format='json')
        assert get_response.status_code == status.HTTP_401_UNAUTHORIZED
        assert get_response.json() is not None

    def test_login_with_no_payload(self, auth_client):
        url = reverse("user:login")
        get_response = auth_client.post(url, format='json')
        assert get_response.status_code == status.HTTP_400_BAD_REQUEST
        assert get_response.json() is not None

    def test_not_allowed_method_does_not_work_in_login_api(self, auth_client):
        url = reverse("user:login")
        get_response = auth_client.get(url)
        assert get_response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        assert get_response.json() is not None

        put_response = auth_client.put(url)
        assert put_response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        assert put_response.json() is not None

        patch_response = auth_client.patch(url)
        assert patch_response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        assert patch_response.json() is not None

        delete_response = auth_client.delete(url)
        assert delete_response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        assert delete_response.json() is not None


class TestUserViewSet:
    def test_get_users_with_unauthentic_client(self, client):
        url = reverse("user:users-list")
        get_response = client.get(url)
        assert get_response.status_code == status.HTTP_401_UNAUTHORIZED
        assert get_response.json() is not None

    def test_get_users_with_authentic_client(self, auth_client):
        url = reverse("user:users-list")
        get_response = auth_client.get(url)
        assert get_response.status_code == status.HTTP_200_OK
        assert get_response.json() is not None

    def test_not_allowed_method_does_not_work_in_user_api(self, auth_client):
        url = reverse("user:users-list")
        post_response = auth_client.post(url)
        assert post_response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        assert post_response.json() is not None

        put_response = auth_client.put(url)
        assert put_response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        assert put_response.json() is not None

        patch_response = auth_client.patch(url)
        assert patch_response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        assert patch_response.json() is not None

        delete_response = auth_client.delete(url)
        assert delete_response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        assert delete_response.json() is not None


class TestPasswordChangeAPIView:
    payload = {
            "email": "new@mail.com",
            "user_type": "Admin",
            "password": "admin@123",
            "password2": "admin@123"
        }
    def test_change_password_with_unauthentic_client(self, client):
        payload = {
            "current_password": "new@mail.com",
            "new_password": "admin@123",
            "new_password2": "admin@123"
        }
        url = reverse("user:password-change")
        post_response = client.post(url, data=payload, format='json')
        assert post_response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_change_password_with_authentic_client(self, auth_client):
        payload = self.payload
        url = reverse("user:register")
        get_response = auth_client.post(url, data=payload, format='json')
        assert get_response.status_code == status.HTTP_201_CREATED
        payload = {
            "current_password": "admin@123",
            "new_password": "admin@1234",
            "new_password2": "admin@1234"
        }
        url = reverse("user:password-change")
        post_response = auth_client.post(url, data=payload, format='json')
        assert post_response.status_code == status.HTTP_200_OK

    def test_change_password_with_non_matching_password(self, auth_client):
        payload = self.payload
        url = reverse("user:register")
        get_response = auth_client.post(url, data=payload, format='json')
        assert get_response.status_code == status.HTTP_201_CREATED
        payload = {
            "current_password": "admin@123",
            "new_password": "admin@124",
            "new_password2": "admin@1234"
        }
        url = reverse("user:password-change")
        post_response = auth_client.post(url, data=payload, format='json')
        assert post_response.status_code == status.HTTP_400_BAD_REQUEST
        assert post_response.json() is not None

    def test_change_password_without_payload(self, auth_client):
        payload = self.payload
        url = reverse("user:register")
        get_response = auth_client.post(url, data=payload, format='json')
        assert get_response.status_code == status.HTTP_201_CREATED

        url = reverse("user:password-change")
        post_response = auth_client.post(url, format='json')
        assert post_response.status_code == status.HTTP_400_BAD_REQUEST
        assert post_response.json() is not None

    def test_not_allowed_method_does_not_work_in_password_change_api(self, auth_client):
        url = reverse("user:password-change")
        get_response = auth_client.get(url)
        assert get_response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        assert get_response.json() is not None

        put_response = auth_client.put(url)
        assert put_response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        assert put_response.json() is not None

        patch_response = auth_client.patch(url)
        assert patch_response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        assert patch_response.json() is not None

        delete_response = auth_client.delete(url)
        assert delete_response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        assert delete_response.json() is not None