from django.db import models

from user_profile.models import User, Candidate, Employer
from vacancy.models import Vacancy


class Chat(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
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