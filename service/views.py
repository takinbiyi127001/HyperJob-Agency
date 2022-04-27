from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.views.generic import View, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from .forms import SignupForm
from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin


# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return render(request, 'service/index.html')
    else:
        return redirect('/home')


class MySignupView(CreateView):
    form_class = SignupForm
    success_url = 'login'
    template_name = 'service/signup.html'


# def signup(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             messages.success(request, "Registration successful.")
#             return redirect("/home")
#         messages.error(request, "Unsuccessful registration. Invalid information")
#     form = SignupForm()
#     return render(request, template_name="service/signup.html", context={"signup_form": form})


class MyLoginView(LoginView):
    # if login is successful redirect user to the menu page
    redirect_authenticated_user = True
    template_name = 'service/login.html'
    # LOGIN_REDIRECT_URL = 'home'


class HomeView(LoginRequiredMixin, View):

    def get(self, request):
        template_name = 'service/home.html'
        # user = request.User.username
        authorised = request.user.is_authenticated
        anonymous = request.user.is_anonymous
        # staff = request.user.is_staff

        if not authorised or anonymous:
            return HttpResponseForbidden()

        return render(request, template_name=template_name)
