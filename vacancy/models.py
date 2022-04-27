from django.db import models
from django.contrib.auth.models import User, Group


# Create your models here.


class Vacancy(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vacancy_author')
    description = models.TextField(max_length=1024)

    # ROLE_CHOICES = (
    #     ('MANAGER', 'Manager'),
    #     ('CANDIDATE', 'Candidate'),
    # )
    # role = models.CharField(max_length=300, choices=ROLE_CHOICES, default='MANAGER')

    # my_group = Group.objects.get(name='Manager')
    # users = User.objects.all()
    # for u in users:
    #     my_group.user_set.add(u)

    class Meta:
        # permissions = [("can_change_vacancy", "can change vacancy"), ("can_add_vacancy", "can add vacancy"),
        #                ("can_delete_vacancy", "can delete vacancy"), ("can_view_vacancy", "can view vacancy")]
        verbose_name_plural = "vacancies"

    def __str__(self):
        return f"{self.author} {self.description}"
