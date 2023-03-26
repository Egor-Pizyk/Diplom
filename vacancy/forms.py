from django import forms

from user_profile.models import User, Employer
from vacancy.models import Vacancy


class VacancyCreateForm(forms.ModelForm):
    employer_id = forms.IntegerField()

    class Meta:
        model = Vacancy
        fields = ['title', 'text', 'requirements', 'country', 'employment_rate', 'month_salary', 'hour_salary', 'experience', 'english_level', 'work_category', 'employer_id']

    def clean_employer_id(self):
        user = User.objects.get(id=self.cleaned_data['employer_id'])
        return Employer.objects.get(user=user.id).id

    def save(self, commit=True):
        return Vacancy.objects.create(**self.cleaned_data)


