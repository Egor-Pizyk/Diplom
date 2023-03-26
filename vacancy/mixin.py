from django.urls import reverse_lazy

from user_profile.choices import ENGLISH_LEVEL, EMPLOYMENT_RATE
from user_profile.models import Country, WorkCategory, WorkType, ContactMethod


class VacanciesDataMixin:

    @property
    def vacancies_tabs(self):
        return [{'tab_name': 'All vacancies', 'tab_url': reverse_lazy('user_profile:my-profile')},
                {'tab_name': 'Vacancies by my profile', 'tab_url': reverse_lazy('user_profile:my-contact')},
                {'tab_name': 'Favorite', 'tab_url': reverse_lazy('user_profile:my-contact')}]
