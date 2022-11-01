from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display= ["id", "name","address"]

admin.site.register(Student, StudentAdmin)