from model_serilizers import views
from django.urls import path,include


urlpatterns = [
    path('model_serilizers_curd_operation/',views.student_api_curd,name="student_api_curd"),
]