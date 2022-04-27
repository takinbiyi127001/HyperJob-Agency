from django.db import models
from django.contrib.auth.models import User, Group


# Create your models here.

class Resume(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resume_author')
    description = models.TextField(max_length=1024)

    # my_group = Group.objects.get(name='Candidate')
    # users = User.objects.all()
    # for u in users:
    #     my_group.user_set.add(u)
    # user = User.objects.get(username=User.username)
    # User.groups.add(my_group)

    class Meta:
        verbose_name_plural = "resumes"
        # permissions = [('can_add_resume', 'Can add resume'), ('can_delete_resume', 'Can delete resume'),
        #                ('can_change_resume', 'Can change resume')]

    def __str__(self):
        return self.description
