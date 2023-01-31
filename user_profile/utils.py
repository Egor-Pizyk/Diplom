from user_profile.models import Candidate


def create_candidate(request):
    Candidate.objects.create(
        user_id=request.user.pk,
        position=request.POST['position'],
        month_salary=request.POST['month_salary'],
        hour_salary=request.POST['hour_salary'],
        experience=request.POST['experience'],
        country_id=int(request.POST['country']),
        is_ready_to_relocate_country=bool(request.POST.get('is_ready_to_relocate_country', False)),
        skills=request.POST['skills'],
        work_category_id=int(request.POST['work_category']),
        english_level=request.POST['english_level'],
        employment_rate=request.POST['employment_rate'],
        about_work_experience=request.POST['about_work_experience'],
        about_work_expectations=request.POST['about_work_expectations'],
        fav_contact_method_id=int(request.POST['fav_contact_method']),
    )


def create_employers():
    pass