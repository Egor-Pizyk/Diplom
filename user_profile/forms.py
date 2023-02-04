from django import forms

from CareerQuest.settings import CV_FILES_PATH, AVATAR_FILES_PATH
from user_profile.choices import ENGLISH_LEVEL, EMPLOYMENT_RATE
from user_profile.models import User, Candidate


class MainDataCandidateProfileForm(forms.ModelForm):
    position = forms.CharField()
    month_salary = forms.IntegerField()
    hour_salary = forms.FloatField()
    experience = forms.FloatField()
    country = forms.IntegerField()
    is_ready_to_relocate_country = forms.BooleanField(required=False)
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


class ContactDataCandidateProfileForm(forms.ModelForm):
    work_email = forms.CharField(max_length=255, required=False)
    skype = forms.CharField(max_length=255, required=False)
    phone = forms.CharField(max_length=255, required=False)
    telegram = forms.CharField(max_length=255, required=False)
    linkedin_url = forms.CharField(max_length=255, required=False)
    github_url = forms.CharField(max_length=255, required=False)
    portfolio_url = forms.CharField(max_length=255, required=False)
    cv_file = forms.FileField(required=False)
    avatar_img = forms.FileField(required=False)

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if Candidate.objects.filter(phone=phone).exists():
            return forms.ValidationError("This phone already used!")

        return phone

    class Meta:
        model = Candidate
        fields = ('work_email',
                  'skype',
                  'phone',
                  'telegram',
                  'linkedin_url',
                  'github_url',
                  'portfolio_url',
                  'cv_file',
                  'avatar_img')
