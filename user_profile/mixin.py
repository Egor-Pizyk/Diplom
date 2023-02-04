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
