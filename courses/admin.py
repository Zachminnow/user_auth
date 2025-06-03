from django.contrib import admin
from .models import Student, Course, Profile


# Register your models here.
admin.site.register(Profile)
admin.site.register(Course)
admin.site.register(Student)
