from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from CareerQuest.settings import CV_FILES_PATH, AVATAR_FILES_PATH
from user_profile.choices import ROLE, ENGLISH_LEVEL, EMPLOYMENT_RATE
from user_profile.managers import UserProfileManager


class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    role = models.CharField(max_length=3, choices=ROLE)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []



