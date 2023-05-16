from django.contrib import admin
from django.urls import path,include
from api import views

urlpatterns = [
    path('student_api/', views.student_detail,name="student_api"),
]
