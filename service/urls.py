from django.urls import path
from django.views.generic import RedirectView
from django.contrib.auth.views import LogoutView

from . import views
from vacancy.views import VacancyView
from resume.views import ResumeView

urlpatterns = [
    path('', views.index),
    path('vacancies', VacancyView.as_view(), name="vacancy"),
    path('resumes', ResumeView.as_view(), name="resume"),
    path('login', views.MyLoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('signup', views.MySignupView.as_view(), name='signup'),
    path('login/', RedirectView.as_view(url='/login')),
    path('logout/', RedirectView.as_view(url='/logout')),
    path('signup/', RedirectView.as_view(url='/signup')),

]