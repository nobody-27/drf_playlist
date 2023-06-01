from django.contrib import admin
from django.urls import path,include
from custom_permission import views
from rest_framework.routers import DefaultRouter


#creating Router Objecet
custom_perm = DefaultRouter()

#register function with router
custom_perm.register('custom_perm',views.Person_list_api,basename="Person_list_api")

urlpatterns = [
    path('',include(custom_perm.urls)),
    
]
