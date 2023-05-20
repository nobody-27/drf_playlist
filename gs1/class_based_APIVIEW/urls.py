from django.urls import path
from class_based_APIVIEW import views

urlpatterns = [
    path('class_based/',views.NoteBook_API.as_view(),name="class_based"),
    path('class_based/<int:pk>/',views.NoteBook_API.as_view(),name="class_based"),
]
