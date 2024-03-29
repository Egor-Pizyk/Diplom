
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

from CareerQuest.settings import CV_FILES_PATH, AVATAR_FILES_PATH, STATIC_URL
from user_profile.choices import ROLE, ENGLISH_LEVEL, EMPLOYMENT_RATE, EMPLOY_COUNT
from user_profile.managers import UserProfileManager


class User(AbstractUser, PermissionsMixin):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    role = models.CharField(max_length=3, choices=ROLE)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_avatar_img(self):
        if self.role == 'CAN' and Candidate.objects.filter(user_id=self.pk).values('avatar_img'):
            return Candidate.objects.filter(user_id=self.pk).values('avatar_img')[0].get('avatar_img').replace('static/', '')
        elif self.role == 'EMP' and Employer.objects.filter(user_id=self.pk).values('avatar_img'):
            return Employer.objects.filter(user_id=self.pk).values('avatar_img')[0].get('avatar_img').replace('static/', '')
        return 'media/defualt_user_icon.svg'

class Candidate(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    work_email = models.EmailField(null=True, blank=True)
    is_active_profile = models.BooleanField(default=True)
    position = models.CharField(max_length=500)
    month_salary = models.PositiveSmallIntegerField(blank=True, null=True)
    hour_salary = models.PositiveSmallIntegerField(blank=True, null=True)
    experience = models.FloatField()
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    is_ready_to_relocate_country = models.BooleanField(blank=True, null=True)
    skills = models.TextField()
    work_category = models.ForeignKey('WorkCategory', on_delete=models.CASCADE)
    english_level = models.CharField(max_length=2, choices=ENGLISH_LEVEL)
    employment_rate = models.CharField(max_length=3, choices=EMPLOYMENT_RATE, blank=True, null=True)
    about_work_experience = models.TextField(blank=True, null=True)
    about_work_expectations = models.TextField(blank=True, null=True)
    fav_contact_method = models.ForeignKey('ContactMethod', on_delete=models.CASCADE, blank=True, null=True)
    skype = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    telegram = models.CharField(max_length=255, blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    portfolio_url = models.URLField(blank=True, null=True)
    cv_file = models.FileField(upload_to=f'{STATIC_URL}{CV_FILES_PATH}', blank=True, null=True)
    avatar_img = models.ImageField(upload_to=f'{STATIC_URL}{AVATAR_FILES_PATH}', blank=True, null=True)

    def __str__(self):
        return f'{self.user.email} {self.user.first_name} {self.user.last_name}'


class Employer(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    company_name = models.CharField(max_length=500)
    about_company = models.TextField()
    position = models.CharField(max_length=255)
    company_url = models.URLField()
    dou_url = models.URLField()
    employ_count = models.CharField(max_length=7, choices=EMPLOY_COUNT)
    avatar_img = models.ImageField(upload_to=f'{STATIC_URL}{AVATAR_FILES_PATH}', blank=True, null=True)


    def __str__(self):
        return f'{self.user.email} {self.user.first_name} {self.user.last_name} - {self.company_name}'


class Country(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class WorkCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    work_type = models.ForeignKey('WorkType', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class WorkType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class ContactMethod(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class MessageTemplate(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    candidate = models.ForeignKey('Candidate', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.candidate.user.first_name} {self.user.last_name} - {self.title}'
