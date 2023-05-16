from django.contrib import admin
from api import models
stu = models.Student
# Register your models here.

@admin.register(stu)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','city','data']