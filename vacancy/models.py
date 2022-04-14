from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Vacancy(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=1024)

    class Meta:
        verbose_name_plural = "vacancies"

    def __str__(self):
        return f"{self.author} {self.description}"
