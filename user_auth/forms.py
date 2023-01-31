from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from user_profile.choices import ROLE
from user_profile.models import User
from django.utils.translation import gettext_lazy as _


class AuthUserForm(AuthenticationForm):
    username = forms.CharField(max_length=255, label='Email')
    password = forms.CharField(max_length=255, label='Password')

    error_messages = {
        'invalid_login': _(
            "Введіть правильний логін і пароль. Врахуйте що обидва поля можуть бути чутливі до регістру."
        ),
    }

    class Meta:
        model = User
        fields = ('username', 'password')


class RegisterUserForm(forms.ModelForm):
    username = forms.EmailField(max_length=30, required=True)
    password1 = forms.CharField(max_length=30, min_length=8, required=True, label='Password')
    password2 = forms.CharField(max_length=30, min_length=8, required=True, label='Password confirmation')
    role = forms.ChoiceField(choices=ROLE)

    def clean_username(self):
        email = self.cleaned_data['username']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(_("This email already used"))
        return email

    def save(self):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data['username'].lower()
        user.role = self.cleaned_data['role']
        user.save()

        return user

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'role')


class UserRemindForm(forms.ModelForm):
    username = forms.EmailField(max_length=30, required=True, error_messages={'wrong': _("Невірний формат email.")})

    def clean_username(self):
        email = self.cleaned_data['username']
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError(f"Користувача з таким email ({email}) не існує.")
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
