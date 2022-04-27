from django.contrib.auth.models import Permission
from django.contrib.auth.views import redirect_to_login
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.views.generic import View, CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType

# Create your views here.
from .models import Resume
from .forms import ResumeForm


class ResumeView(View):
    template_name = 'resume/resume.html'

    def get(self, request):
        resumes = Resume.objects.all()
        context = {
            'resumes': resumes
        }
        return render(request, template_name=self.template_name, context=context)


# class UserAccessMixin(PermissionRequiredMixin):
#
#     def dispatch(self, request, *args, **kwargs):
#         if not request.user.is_authenticated:
#             return redirect_to_login(request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())
#         # if request.user.is_staff:
#         #     return redirect('/home')
#         return super(UserAccessMixin, self).dispatch(request, *args, **kwargs)


class CreateResumeView(LoginRequiredMixin, CreateView):
    model = Resume
    form = ResumeForm
    login_url = '/login'
    raise_exception = False
    # permission_required = ("resume.add_resume", "resume.change_resume")
    redirect_field_name = 'login'

    fields = ["description"]
    # fields = "__all__"
    template_name = 'resume/create_resume.html'
    success_url = '/resumes'

    def get(self, request, *args, **kwargs):
        if request.user.is_staff:
            return HttpResponseForbidden()
        return super(CreateResumeView, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        # super(CreateResumeView, self).form_valid(form)
        # return redirect('/resumes')
