from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DeleteView

from user_profile.choices import ENGLISH_LEVEL, EMPLOYMENT_RATE
from user_profile.forms import AdditionalDataToCandidateProfileForm
from user_profile.mixin import UserProfileFormDataMixin
from user_profile.models import Country, WorkCategory, ContactMethod, WorkType, User, Candidate
from user_profile.utils import create_candidate, create_employers


class FillMyProfile(UserProfileFormDataMixin, TemplateView):
    template_name = 'user_profile/profile.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        form = AdditionalDataToCandidateProfileForm(instance=user)
        context = self.get_context_data({'form': form})
        return render(request, 'user_profile/profile.html', context)

    def post(self, request):
        form = AdditionalDataToCandidateProfileForm(request.POST)
        context = self.get_context_data()
        if form.is_valid():
            if request.user.role == 'CAN':
                create_candidate(request)
            else:
                create_employers()

            return redirect('user_profile:success')

        context['form'] = form
        return render(request, 'user_profile/profile.html', context)


def remove_m_profile(request):
    if request.method == "POST":
        User.objects.filter(pk=request.user.pk).delete()

        return redirect('user_auth:user-login')


def index(request):
    HttpResponse('ok')
