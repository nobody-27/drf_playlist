from django.urls import path,include
from function_based import views
urlpatterns = [
    path('function_based/',views.hello_world),
    path('notebook_api/',views.notebook_api,name="notebook")
]