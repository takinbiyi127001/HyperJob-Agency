from django.contrib import admin

# Register your models here.
from resume.models import Resume
from vacancy.models import Vacancy


class ServiceAdmin(admin.ModelAdmin):
    list_display = ("author", "description",)
    # fieldsets = [(None, {'fields': ('username', 'password')})]
    # list_filter = ("user", "description")


admin.site.register(Resume, ServiceAdmin)
admin.site.register(Vacancy, ServiceAdmin)

# superuser -> akint -- ering1
