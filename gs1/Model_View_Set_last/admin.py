from django.contrib import admin
from Model_View_Set_last.models import ClassRoom
# Register your models here.


@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):
    list_display = ['id','name','class_url','city']
    
