from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DeleteView, ListView

from CareerQuest.settings import LOGIN_URL
from user_profile.choices import ENGLISH_LEVEL, EMPLOYMENT_RATE
from user_profile.forms import MainDataCandidateProfileForm, ContactDataCandidateProfileForm, \
    MainDataEmployerProfileForm, ContactDataEmployerProfileForm
from user_profile.mixin import UserProfileFormDataMixin
from user_profile.models import Country, WorkCategory, ContactMethod, WorkType, User, Candidate, Employer
from user_profile.utils import update_or_create_candidate, update_candidate, update_or_create_employer, update_employer


class FillMainInfoProfile(LoginRequiredMixin, UserProfileFormDataMixin, TemplateView):
    login_url = LOGIN_URL
    redirect_field_name = 'user_profile:my-profile'

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.first_name != '':
            if user.role == 'CAN':
                user = Candidate.objects.get(user_id=user.pk)
            else:
                user = Employer.objects.get(user_id=user.pk)

        form = MainDataCandidateProfileForm()

        context = self.get_custom_context_form_data({'form': form})
        context = self.get_filled_candidate_profile_form(user, context)
        context['tabs'] = self.profile_tabs
        context['selected_tab'] = 'Profile'

        return render(request, 'user_profile/profile.html', context)

    def post(self, request):
        context = self.get_custom_context_form_data()
        if request.user.role == 'CAN':
            form = MainDataCandidateProfileForm(request.POST)
            update_or_create = update_or_create_candidate
        else:
            form = MainDataEmployerProfileForm(request.POST)
            update_or_create = update_or_create_employer

        if form.is_valid():
            update_or_create(request)

            if request.user.first_name:
                return redirect('user_profile:my-profile')
            else:
                return redirect('user_profile:my-contact')

        context['form'] = form
        return render(request, 'user_profile/profile.html', context)


class FillContactProfile(LoginRequiredMixin, UserProfileFormDataMixin, TemplateView):
    login_url = LOGIN_URL
    redirect_field_name = 'user_profile:my-contact'

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.first_name != '':
            if user.role == 'CAN':
                user = Candidate.objects.get(user_id=user.pk)
            else:
                user = Employer.objects.get(user_id=user.pk)

        form = ContactDataCandidateProfileForm()
        context = {'form': form}

        if user.user.first_name:
            context = self.get_filled_candidate_contacts_form(user, context)

        context['tabs'] = self.profile_tabs
        context['selected_tab'] = 'Contacts'

        return render(request, 'user_profile/contact.html', context)

    def post(self, request, *args, **kwargs):
        # context = self.get_custom_context_form_data()
        if request.user.role == 'CAN':
            candidate_phone = Candidate.objects.get(user_id=request.user.pk).phone
            post_data = request.POST.copy()

            if candidate_phone == post_data['phone']:
                post_data.pop('phone', None)

            form = ContactDataCandidateProfileForm(post_data, request.FILES)
            update_or_create = update_candidate
        else:
            form = ContactDataEmployerProfileForm(request.POST)
            update_or_create = update_employer

        context = {}

        if form.is_valid():
            update_or_create(request)

            return redirect('user_profile:my-contact')

        context['form'] = form
        return render(request, 'user_profile/contact.html', context)

@login_required(redirect_field_name='user_profile:my-profile')
def remove_m_profile(request):
    if request.method == "GET":
        User.objects.filter(pk=request.user.pk).delete()

        return redirect('user_auth:user-login')


def index(request):
    HttpResponse('ok')
