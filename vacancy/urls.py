from django.urls import path

from vacancy.views import VacancyList, VacancyDetail, EmployerVacanciesList, VacancyCreate

app_name = 'vacancy'

urlpatterns = [
    path('vacancy-list/', VacancyList.as_view(), name='vacancy-list'),
    path('vacancy-detail/<int:pk>/', VacancyDetail.as_view(), name='vacancy-detail'),

    path('vacancy-create/', VacancyCreate.as_view(), name='vacancy-create'),

    path('employer-vacancies-list/', EmployerVacanciesList.as_view(), name='employer-vacancies-list')

]
