from django.contrib import admin
from Token_Authentication.models import Token_Testing



#  Register your models here.


@admin.register(Token_Testing)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll','description']
    
