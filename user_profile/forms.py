from django import forms

from user_profile.choices import ENGLISH_LEVEL, EMPLOYMENT_RATE
from user_profile.models import User, Candidate


class AdditionalDataToCandidateProfileForm(forms.ModelForm):
    position = forms.CharField()
    month_salary = forms.IntegerField()
    hour_salary = forms.FloatField()
    experience = forms.FloatField()
    country = forms.IntegerField()
    is_ready_to_relocate_country = forms.BooleanField()
    skills = forms.CharField()
    work_category = forms.IntegerField()
    english_level = forms.CharField()
    employment_rate = forms.CharField()
    about_work_experience = forms.CharField()
    about_work_expectations = forms.CharField()
    fav_contact_method = forms.IntegerField()

    class Meta:
        model = Candidate
        fields = ('position',
                  'month_salary',
                  'experience',
                  'country',
                  'is_ready_to_relocate_country',
                  'skills',
                  'work_category',
                  'english_level',
                  'employment_rate',
                  'about_work_experience',
                  'about_work_expectations',
                  'fav_contact_method')
