import base64
import os

from django.contrib.auth import logout
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from dotenv import load_dotenv

from CareerQuest.settings import SHORT_DJANGO_KEY
from user_auth.forms import AuthUserForm, RegisterUserForm, UpdateUserPasswordForm, UserRemindForm
from user_auth.utils import send_email
from user_profile.models import User
from cryptography.fernet import Fernet


def to_login_redirect(request):
    if isinstance(request.user, AnonymousUser):
        return redirect('user_auth:user-login')
    else:
        return redirect('user_profile:my-profile')


class UserLoginView(LoginView):
    form_class = AuthUserForm
    template_name = 'user_auth/login.html'

    def get_success_url(self):
        if self.request.user.first_name == '':
            return reverse_lazy('user_profile:my-profile')
        else:
            return reverse_lazy('user_auth:success')


def user_logout(request):
    logout(request)
    return redirect('user_auth:user-login')


class UserRegisterView(CreateView):
    form_class = RegisterUserForm
    template_name = 'user_auth/register.html'
    success_url = reverse_lazy('user_auth:user-login')


class UserRemindView(TemplateView):
    template_name = 'user_auth/remind.html'

    def post(self, request, *args, **kwargs):
        context = {}
        form = UserRemindForm(request.POST)
        if form.is_valid():
            fernet = Fernet(base64.b64encode(str.encode(SHORT_DJANGO_KEY)))
            user = User.objects.get(email=request.POST['username'])
            code = fernet.encrypt(str.encode(str(user.pk)))
            send_email(user.email, code)
            return redirect('user_auth:success')
        context['form'] = form
        return render(request, 'user_auth/remind.html', context)


class UserResetPasswordView(TemplateView):
    template_name = 'user_auth/reset_password.html'

    def post(self, request, *args, **kwargs):
        form = UpdateUserPasswordForm(request.POST)
        context = {}
        if form.is_valid():
            fernet = Fernet(base64.b64encode(str.encode(os.getenv('SHORT_DJANGO_KEY'))))
            code = fernet.decrypt(str.encode(str(self.kwargs['code'])))
            user = User.objects.get(pk=code.decode())
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return redirect('user_auth:user-login')
        context['form'] = form
        return render(request, 'user_auth/reset_password.html', context)


def success(requests):
    return HttpResponse('ok')
