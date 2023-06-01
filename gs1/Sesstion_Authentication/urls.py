from django.contrib import admin
from django.urls import path,include
from Sesstion_Authentication import views
from rest_framework.routers import DefaultRouter

#create object
sesstion_auth = DefaultRouter()

#register function with urls 
sesstion_auth.register('person_api',views.PersonModelViewSet,basename="person_api")

urlpatterns = [
    path('',include(sesstion_auth.urls))
]
