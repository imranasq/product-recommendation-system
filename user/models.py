from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser
from .manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    USER_TYPE_CHOICES = (
        ('Admin', 'Admin'),
        ('Vendor', 'Vendor'),
        ('Customer', 'Customer'),
    )
    username = models.CharField("username", max_length=30, unique=True, null=True, blank=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, null=True, blank=True)
    email = models.EmailField("email address", blank=True, unique=True)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField('Date Joined', auto_now_add=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    # profile_pic = models.ImageField(default='default.png', upload_to='images/profile/')
    bio = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.email
