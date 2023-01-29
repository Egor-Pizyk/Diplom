from django.db import models

from user_profile.choices import EMPLOYMENT_RATE, ENGLISH_LEVEL
from user_profile.models import User, Candidate, Employer, WorkCategory, Country


class Vacancy(models.Model):
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField()
    requirements = models.TextField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    employment_rate = models.CharField(max_length=3, choices=EMPLOYMENT_RATE)
    month_salary = models.PositiveSmallIntegerField()
    hour_salary = models.PositiveSmallIntegerField()
    experience = models.FloatField()
    english_level = models.CharField(max_length=2, choices=ENGLISH_LEVEL)
    work_category = models.ForeignKey(WorkCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.employer.company_name} - {self.title}'


class Chat(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    vacancy = models.ForeignKey('Vacancy', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.candidate.user.first_name} - {self.vacancy.employer.company_name}'


class ChatMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chat = models.ForeignKey('Chat', on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text