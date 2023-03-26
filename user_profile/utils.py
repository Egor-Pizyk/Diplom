from user_profile.models import Candidate, Employer


def update_or_create_candidate(request):
    Candidate.objects.update_or_create(
        user_id=request.user.pk,
        defaults={
            'position': request.POST.get('position'),
            'month_salary': request.POST.get('month_salary'),
            'hour_salary': request.POST.get('hour_salary'),
            'experience': request.POST.get('experience'),
            'country_id': int(request.POST.get('country_id')),
            'is_ready_to_relocate_country': bool(request.POST.get('is_ready_to_relocate_country', False)),
            'skills': request.POST.get('skills'),
            'work_category_id': int(request.POST.get('work_category_id')),
            'english_level': request.POST.get('english_level'),
            'employment_rate': request.POST.get('employment_rate'),
            'about_work_experience': request.POST.get('about_work_experience'),
            'about_work_expectations': request.POST.get('about_work_expectations'),
            'fav_contact_method_id': int(request.POST.get('fav_contact_method_id')),
        }
    )


def update_or_create_employer(request):
    Employer.objects.update_or_create(
        user_id=request.user.pk,
        defaults={
            'company_name': request.POST.get('company_name'),
            'about_company': request.POST.get('about_company'),
            'position': request.POST.get('position'),
            'company_url': request.POST.get('company_url'),
            'dou_url': request.POST.get('dou_url'),
            'employ_count': request.POST.get('employ_count'),
        }
    )


def update_candidate(request):
    Candidate.objects.filter(user__pk=request.user.pk).update(
        work_email=request.POST.get('work_email'),
        skype=request.POST.get('skype'),
        phone=request.POST.get('phone'),
        telegram=request.POST.get('telegram'),
        linkedin_url=request.POST.get('linkedin_url'),
        github_url=request.POST.get('github_url'),
        portfolio_url=request.POST.get('portfolio_url'),
    )

    candidate = Candidate.objects.get(user__pk=request.user.pk)
    if request.FILES.get('cv_file', None):
        candidate.cv_file = request.FILES['cv_file']

    if request.FILES.get('avatar_img', None):
        candidate.avatar_img = request.FILES['avatar_img']

    candidate.save()

    if request.POST.get('first_name') or request.POST.get('last_name'):
        candidate.user.first_name = request.POST.get('first_name')
        candidate.user.last_name = request.POST.get('last_name')

        candidate.user.save()


def update_employer(request):
    employer = Employer.objects.get(user__pk=request.user.pk)

    if request.FILES.get('avatar_img', None):
        employer.avatar_img = request.FILES['avatar_img']

    employer.save()

    if request.POST.get('first_name') or request.POST.get('last_name'):
        employer.user.first_name = request.POST.get('first_name')
        employer.user.last_name = request.POST.get('last_name')

        employer.user.save()

