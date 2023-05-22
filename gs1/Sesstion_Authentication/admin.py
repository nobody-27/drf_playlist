from django.contrib import admin
from Sesstion_Authentication.models import Person
# Register your models here.



@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll','bio']
    

