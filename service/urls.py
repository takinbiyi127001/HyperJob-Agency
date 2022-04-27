from django.urls import path
from django.views.generic import RedirectView
from django.contrib.auth.views import LogoutView

from . import views
from vacancy.views import VacancyView, CreateVacancyView
from resume.views import ResumeView, CreateResumeView

urlpatterns = [
    path('', views.index),
    path('vacancies', VacancyView.as_view(), name="vacancy"),
    path('vacancy/new', CreateVacancyView.as_view(), name="create_vacancy"),
    path('resumes', ResumeView.as_view(), name="resume"),
    path('resume/new', CreateResumeView.as_view(), name="create_resume"),
    path('login', views.MyLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('signup', views.MySignupView.as_view(), name='signup'),
    # path('signup', views.signup, name='signup'),
    path('home', views.HomeView.as_view(), name='home'),
    path('login/', RedirectView.as_view(url='/login')),
    path('logout/', RedirectView.as_view(url='/logout')),
    path('signup/', RedirectView.as_view(url='/signup')),

]
