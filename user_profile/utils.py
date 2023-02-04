from user_profile.models import Candidate


def create_candidate(request):
    Candidate.objects.create(
        user_id=request.user.pk,
        position=request.POST.get('position'),
        month_salary=request.POST.get('month_salary'),
        hour_salary=request.POST.get('hour_salary'),
        experience=request.POST.get('experience'),
        country_id=int(request.POST.get('country')),
        is_ready_to_relocate_country=bool(request.POST.get('is_ready_to_relocate_country', False)),
        skills=request.POST.get('skills'),
        work_category_id=int(request.POST.get('work_category')),
        english_level=request.POST.get('english_level'),
        employment_rate=request.POST.get('employment_rate'),
        about_work_experience=request.POST.get('about_work_experience'),
        about_work_expectations=request.POST.get('about_work_expectations'),
        fav_contact_method_id=int(request.POST.get('fav_contact_method')),
    )


def create_employers():
    pass


def update_candidate(request):
    Candidate.objects.filter(user__pk=request.user.pk).update(
        work_email=request.POST.get('work_email', None),
        skype=request.POST.get('skype', None),
        phone=request.POST.get('phone', None),
        telegram=request.POST.get('telegram', None),
        linkedin_url=request.POST.get('linkedin_url', None),
        github_url=request.POST.get('github_url', None),
        portfolio_url=request.POST.get('portfolio_url', None),
    )

    candidate = Candidate.objects.get(user__pk=request.user.pk)
    if candidate.cv_file:
        candidate.cv_file = request.FILES['cv_file']
        candidate.save()

    if candidate.avatar_img:
        candidate.avatar_img = request.FILES['avatar_img']
        candidate.save()
