from django.urls import reverse_lazy

from user_profile.choices import ENGLISH_LEVEL, EMPLOYMENT_RATE, EMPLOY_COUNT
from user_profile.models import Country, WorkCategory, WorkType, ContactMethod


class UserProfileFormDataMixin:
    @property
    def profile_tabs(self):
        if self.request.user.role == 'CAN':
            return [{'tab_name': 'Profile', 'tab_url': reverse_lazy('user_profile:my-profile')},
                    {'tab_name': 'Contacts', 'tab_url': reverse_lazy('user_profile:my-contact')},
                    {'tab_name': 'Stop-list', 'tab_url': reverse_lazy('user_profile:my-contact')},
                    {'tab_name': 'Offers', 'tab_url': reverse_lazy('user_profile:my-contact')}]
        else:
            return [{'tab_name': 'Profile', 'tab_url': reverse_lazy('user_profile:my-profile')},
                    {'tab_name': 'Contacts', 'tab_url': reverse_lazy('user_profile:my-contact')},
                    {'tab_name': 'Vacancies', 'tab_url': reverse_lazy('vacancy:employer-vacancies-list')}]

    def get_custom_context_form_data(self, old_context=None):
        if old_context is None:
            old_context = {}

        context = {'country_list': Country.objects.all(),
                   'work_category_list': WorkCategory.objects.all(),
                   'work_type_list': WorkType.objects.all(),
                   'fav_contact_method_list': ContactMethod.objects.all(),
                   'english_level_list': ENGLISH_LEVEL,
                   'employment_rate_list': EMPLOYMENT_RATE,
                   'employ_count_list': EMPLOY_COUNT}

        return context | old_context

    @staticmethod
    def get_empty():
        return ''

    def get_filled_candidate_profile_form(self, user, old_context=None):
        new_context = {
            'user_position': getattr(user, 'position', self.get_empty),
            'user_month_salary': getattr(user, 'month_salary', self.get_empty),
            'user_hour_salary': getattr(user, 'hour_salary', self.get_empty),
            'user_experience': getattr(user, 'experience', self.get_empty),
            'user_country_id': getattr(user, 'country_id', self.get_empty),
            'user_is_ready_to_relocate_country': getattr(user, 'is_ready_to_relocate_country', self.get_empty),
            'user_skills': getattr(user, 'skills', self.get_empty),
            'user_work_category_id': getattr(user, 'work_category_id', self.get_empty),
            'user_english_level': getattr(user, 'english_level', self.get_empty),
            'user_employment_rate': getattr(user, 'employment_rate', self.get_empty),
            'user_about_work_experience': getattr(user, 'about_work_experience', self.get_empty),
            'user_about_work_expectations': getattr(user, 'about_work_expectations', self.get_empty),
            'user_fav_contact_method_id': getattr(user, 'fav_contact_method_id', self.get_empty),

            'user_company_name': getattr(user, 'company_name', self.get_empty),
            'user_about_company': getattr(user, 'about_company', self.get_empty),
            'user_company_url': getattr(user, 'company_url', self.get_empty),
            'user_dou_url': getattr(user, 'dou_url', self.get_empty),
            'user_employ_count': getattr(user, 'employ_count', self.get_empty),
        }

        if old_context is not None:
            return new_context | old_context
        return new_context

    def get_filled_candidate_contacts_form(self, user, old_context=None):
        new_context = {
            'first_name': getattr(user.user, 'first_name', self.get_empty),
            'last_name': getattr(user.user, 'last_name', self.get_empty),
            'work_email': getattr(user, 'work_email', self.get_empty),
            'skype': getattr(user, 'skype', self.get_empty),
            'phone': getattr(user, 'phone', self.get_empty),
            'telegram': getattr(user, 'telegram', self.get_empty),
            'linkedin_url': getattr(user, 'linkedin_url', self.get_empty),
            'github_url': getattr(user, 'github_url', self.get_empty),
            'portfolio_url': getattr(user, 'portfolio_url', self.get_empty),
        }

        if old_context is not None:
            return new_context | old_context
        return new_context

