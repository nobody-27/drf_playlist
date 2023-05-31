from django.urls import path,include
from Token_Authentication import views
from rest_framework.routers import DefaultRouter

#create object
token_auth = DefaultRouter()

#register function with urls 
token_auth.register('token',views.Testing_Model,basename="Testing_Model")

urlpatterns = [
    path('',include(token_auth.urls))
]
