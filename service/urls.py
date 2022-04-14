from django.urls import path

from . import views
from vacancy.views import VacancyView
from resume.views import ResumeView

urlpatterns = [
    path('', views.index),
    path('vacancies', VacancyView.as_view(), name="vacancy"),
    path('resumes', ResumeView.as_view(), name="resume")
]