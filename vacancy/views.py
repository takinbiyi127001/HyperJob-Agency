from django.shortcuts import render
from django.views.generic import View

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
