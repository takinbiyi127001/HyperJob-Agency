from django.shortcuts import render
from django.views.generic import View

# Create your views here.
from resume.models import Resume


class ResumeView(View):
    template_name = 'resume/resume.html'

    def get(self, request):
        resumes = Resume.objects.all()
        context = {
            'resumes': resumes
        }
        return render(request, template_name=self.template_name, context=context)


