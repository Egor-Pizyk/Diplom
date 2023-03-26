from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView

from CareerQuest.settings import LOGIN_URL
from user_profile.mixin import UserProfileFormDataMixin
from vacancy.forms import VacancyCreateForm
from vacancy.mixin import VacanciesDataMixin
from vacancy.models import Vacancy


def index(request):
    HttpResponse('ok')


class VacancyList(LoginRequiredMixin, VacanciesDataMixin, ListView):
    login_url = LOGIN_URL
    redirect_field_name = 'user_profile:my-contact'
    template_name = 'vacancy/vacancy_list.html'
    queryset = Vacancy.objects.all()
    context_object_name = 'vacancies'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['tabs'] = self.vacancies_tabs
        context['selected_tab'] = 'All vacancies'

        return context


class VacancyDetail(LoginRequiredMixin, DetailView):
    login_url = LOGIN_URL
    redirect_field_name = 'user_profile:my-contact'
    template_name = 'vacancy/vacancy_detail.html'
    context_object_name = 'vacancy'
    queryset = Vacancy.objects.all()


class EmployerVacanciesList(LoginRequiredMixin, UserProfileFormDataMixin, ListView):
    login_url = LOGIN_URL
    redirect_field_name = 'user_profile:my-contact'
    template_name = 'vacancy/vacancies.html'
    context_object_name = 'vacancies'

    def get_queryset(self):
        return Vacancy.objects.filter(employer__in=self.request.user.employer_set.values_list('id', flat=True))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['tabs'] = self.profile_tabs
        context['selected_tab'] = 'Vacancies'

        return context


class VacancyCreate(LoginRequiredMixin, UserProfileFormDataMixin, CreateView):
    login_url = LOGIN_URL
    redirect_field_name = 'user_profile:my-contact'
    template_name = 'vacancy/create.html'
    form_class = VacancyCreateForm
    context_object_name = 'vacancy'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context = self.get_custom_context_form_data(context)
        return context
