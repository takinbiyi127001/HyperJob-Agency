from django.contrib.auth.views import redirect_to_login
from django.shortcuts import render, redirect
from django.views.generic import View, CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin

# Create your views here.
from vacancy.models import Vacancy


class VacancyView(View):
    template_name = 'vacancy/vacancy.html'

    def get(self, request):
        vacancies = Vacancy.objects.all()
        context = {
            'vacancies': vacancies
        }
        return render(request, template_name=self.template_name, context=context)


class UserAccessMixin(PermissionRequiredMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect_to_login(request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())
        # if request.user.is_staff:
        #     return redirect('/home')

        return super(UserAccessMixin, self).dispatch(request, *args, **kwargs)


class CreateVacancyView(PermissionRequiredMixin, CreateView):
    raise_exception = False
    login_url = '/login'
    permission_required = ("vacancy.add_vacancy", "vacancy.change_vacancy")
    model = Vacancy
    fields = ["description"]
    # fields = "__all__"

    template_name = 'vacancy/create_vacancy.html'
    success_url = '/vacancies'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        # super(CreateVacancyView, self).form_valid(form)
        # return redirect('/vacancies')
