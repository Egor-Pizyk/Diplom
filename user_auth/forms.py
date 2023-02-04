from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import make_password

from user_profile.choices import ROLE
from user_profile.models import User
from django.utils.translation import gettext_lazy as _


class AuthUserForm(AuthenticationForm):
    username = forms.CharField(max_length=255, label='Email', error_messages={'required': 'Email field is required.'})
    password = forms.CharField(max_length=255, label='Password', error_messages={'required': 'Password field is required.'})

    error_messages = {
        'invalid_login': _(
            "Email or password is wrong!"
        ),
    }

    class Meta:
        model = User
        fields = ('username', 'password')


class RegisterUserForm(forms.ModelForm):
    username = forms.EmailField(max_length=30, required=True, error_messages={'required': 'Email field is required!', 'invalid': 'Enter a valid email address!', 'wrong': _("Wrong email format.")})
    password1 = forms.CharField(max_length=30, min_length=8, required=True, label='Password', error_messages={'required': 'Password field is required!'})
    password2 = forms.CharField(max_length=30, min_length=8, required=True, label='Password confirmation', error_messages={'required': 'Password confirmation field is required!'})
    role = forms.ChoiceField(choices=ROLE, required=True, error_messages={'required': 'Role was not selected'})

    def clean_username(self):
        email = self.cleaned_data['username']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(_("This email already used!"))
        return email

    def clean_password1(self):
        password1 = self.data['password1']
        password2 = self.data['password2']
        if password1 != password2:
            raise forms.ValidationError(_("Passwords is not the same!"))

    def save(self):
        user = super(RegisterUserForm, self).save(commit=False)
        user.password = make_password(self.data['password1'])
        user.email = self.cleaned_data['username'].lower()
        user.role = self.data['role']
        user.save()

        return user

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'role')


class UserRemindForm(forms.ModelForm):
    username = forms.EmailField(max_length=30, required=True, error_messages={'wrong': _("Wrong email format."), 'invalid': 'Enter a valid email address!'})

    def clean_username(self):
        email = self.cleaned_data['username']
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError(f"This email ({email}) already exist.")
        return email

    class Meta:
        model = User
        fields = ('username',)


class UpdateUserPasswordForm(forms.ModelForm):
    password1 = forms.CharField(max_length=30, min_length=8, required=True, label='Password')
    password2 = forms.CharField(max_length=30, min_length=8, required=True, label='Password confirmation')

    class Meta:
        model = User
        fields = ('password1', 'password2')
