from user_profile.choices import ENGLISH_LEVEL, EMPLOYMENT_RATE
from user_profile.models import Country, WorkCategory, WorkType, ContactMethod


class UserProfileFormDataMixin:
    def get_custom_context_data(self, old_context=None):
        if old_context is None:
            old_context = {}

        context = {'country_list': Country.objects.all(),
                   'work_category_list': WorkCategory.objects.all(),
                   'work_type_list': WorkType.objects.all(),
                   'fav_contact_method_list': ContactMethod.objects.all(),
                   'english_level_list': ENGLISH_LEVEL,
                   'employment_rate_list': EMPLOYMENT_RATE}

        return context | old_context

    @staticmethod
    def get_empty():
        return ''

    def get_filled_candidate_form(self, candidate, old_context=None):
        new_context = {
            'user_position': getattr(candidate, 'position', self.get_empty),
            'user_month_salary': getattr(candidate, 'month_salary', self.get_empty),
            'user_hour_salary': getattr(candidate, 'hour_salary', self.get_empty),
            'user_experience': getattr(candidate, 'experience', self.get_empty),
            'user_country_id': getattr(candidate, 'country_id', self.get_empty),
            'user_is_ready_to_relocate_country': getattr(candidate, 'is_ready_to_relocate_country', self.get_empty),
            'user_skills': getattr(candidate, 'skills', self.get_empty),
            'user_work_category_id': getattr(candidate, 'work_category_id', self.get_empty),
            'user_english_level': getattr(candidate, 'english_level', self.get_empty),
            'user_employment_rate': getattr(candidate, 'employment_rate', self.get_empty),
            'user_about_work_experience': getattr(candidate, 'about_work_experience', self.get_empty),
            'user_about_work_expectations': getattr(candidate, 'about_work_expectations', self.get_empty),
            'user_fav_contact_method_id': getattr(candidate, 'fav_contact_method_id', self.get_empty),
        }

        if old_context is not None:
            return new_context | old_context
        return new_context
