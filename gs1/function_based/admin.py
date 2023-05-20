from django.contrib import admin
from function_based.models import NoteBook
# Register your models here.


@admin.register(NoteBook)
class NotebookAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll','city']