from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.forms import ModelForm
from resume.models import Resume


class SignupForm(UserCreationForm):
    # ROLE_CHOICES = [
    #     ('MANAGER', 'Manager'),
    #     ('CANDIDATE', 'Candidate'),
    # ]
    # role = forms.ChoiceField(choices=ROLE_CHOICES)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

    # def save(self, commit=True):
    #     user = super(LoginForm, self).save(commit=False)
    #     user.email = self.cleaned_data['email']
    #     # my_group = Group.objects.get(name=f'{self.role}')
    #     # user.role = self.cleaned_data['role']
    #     # print(user.role)
    #     # user.groups.add(user.role)
    #     # User.groups.add(my_group)
    #     if commit:
    #         user.save()
    #     return user
