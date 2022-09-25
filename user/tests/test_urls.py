import pytest
from django.urls import resolve, reverse

pytestmark = pytest.mark.django_db


def test_users_list_url():
    assert reverse("user:users-list") == "/users/"
    assert resolve("/users/").view_name == "user:users-list"


def test_user_profile_list_url():
    assert reverse("user:user-profiles-list") == "/profile/"
    assert resolve("/profile/").view_name == "user:user-profiles-list"


def test_user_login_url():
    assert reverse("user:login") == "/user/login/"
    assert resolve("/user/login/").view_name == "user:login"


def test_user_registration_url():
    assert reverse("user:register") == "/user/register/"
    assert resolve("/user/register/").view_name == "user:register"


def test_user_password_change_url():
    assert reverse("user:password-change") == "/user/change-password/"
    assert resolve("/user/change-password/").view_name == "user:password-change"
