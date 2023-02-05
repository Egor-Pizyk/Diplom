from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DeleteView

from CareerQuest.settings import LOGIN_URL
from user_profile.choices import ENGLISH_LEVEL, EMPLOYMENT_RATE
from user_profile.forms import MainDataCandidateProfileForm, ContactDataCandidateProfileForm
from user_profile.mixin import UserProfileFormDataMixin
from user_profile.models import Country, WorkCategory, ContactMethod, WorkType, User, Candidate
from user_profile.utils import update_or_create_candidate, create_employers, update_candidate


class FillMainInfoProfile(LoginRequiredMixin, UserProfileFormDataMixin, TemplateView):
    login_url = LOGIN_URL
    redirect_field_name = 'user_profile:my-profile'

    def get(self, request, *args, **kwargs):
        user = request.user
        candidate = Candidate.objects.get(user_id=user.pk)
        form = MainDataCandidateProfileForm()

        context = self.get_custom_context_data({'form': form})
        if candidate:
            context = self.get_filled_candidate_form(candidate, context)

        return render(request, 'user_profile/profile.html', context)

    def post(self, request):
        form = MainDataCandidateProfileForm(request.POST)
        context = self.get_custom_context_data()
        if form.is_valid():
            if request.user.role == 'CAN':
                update_or_create_candidate(request)
            else:
                create_employers()

            if request.user.first_name:
                return redirect('user_profile:my-profile')
            else:
                return redirect('user_profile:my-contact')

        context['form'] = form
        return render(request, 'user_profile/profile.html', context)


class FillContactProfile(LoginRequiredMixin, TemplateView):
    login_url = LOGIN_URL
    redirect_field_name = 'user_profile:my-contact'

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

            return redirect('user_profile:my-contact')

        context['form'] = form
        return render(request, 'user_profile/contact.html', context)


@login_required(redirect_field_name='user_profile:my-profile')
def remove_m_profile(request):
    if request.method == "POST":
        User.objects.filter(pk=request.user.pk).delete()

        return redirect('user_auth:user-login')


def index(request):
    HttpResponse('ok')
