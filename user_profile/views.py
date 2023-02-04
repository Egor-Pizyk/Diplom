from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DeleteView

from user_profile.choices import ENGLISH_LEVEL, EMPLOYMENT_RATE
from user_profile.forms import MainDataCandidateProfileForm, ContactDataCandidateProfileForm
from user_profile.mixin import UserProfileFormDataMixin
from user_profile.models import Country, WorkCategory, ContactMethod, WorkType, User, Candidate
from user_profile.utils import create_candidate, create_employers, update_candidate


class FillMainInfoProfile(UserProfileFormDataMixin, TemplateView):

    def get(self, request, *args, **kwargs):
        user = request.user
        form = MainDataCandidateProfileForm(instance=user)
        context = self.get_custom_context_data({'form': form})
        return render(request, 'user_profile/profile.html', context)

    def post(self, request):
        form = MainDataCandidateProfileForm(request.POST)
        context = self.get_custom_context_data()
        if form.is_valid():
            if request.user.role == 'CAN':
                create_candidate(request)
            else:
                create_employers()

            return redirect('user_profile:my-contact')

        context['form'] = form
        return render(request, 'user_profile/profile.html', context)


class FillContactProfile(TemplateView):

    def get(self, request, *args, **kwargs):
        user = request.user
        form = ContactDataCandidateProfileForm(instance=user)
        context = {'form': form}
        return render(request, 'user_profile/contact.html', context)

    def post(self, request, *args, **kwargs):
        form = ContactDataCandidateProfileForm(request.POST, request.FILES)
        context = {}
        if form.is_valid():
            update_candidate(request)

            return redirect('user_profile:success')

        context['form'] = form
        return render(request, 'user_profile/contact.html', context)


def remove_m_profile(request):
    if request.method == "POST":
        User.objects.filter(pk=request.user.pk).delete()

        return redirect('user_auth:user-login')


def index(request):
    HttpResponse('ok')
