from django.shortcuts import render
from django.views.generic import View, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView


# Create your views here.

def index(request):
    return render(request, 'service/index.html')


class MySignupView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'service/signup.html'


class MyLoginView(LoginView):
    # if login is successful redirect user to the menu page
    redirect_authenticated_user = True
    template_name = 'service/login.html'



