from django.contrib import admin
from django.urls import path,include
from BasicAuthentication import views
from rest_framework.routers import DefaultRouter


#creating Router Objecet
auth_api = DefaultRouter()

#register function with router
auth_api.register('auth_api',views.Api_for_Authentication,basename="Auth_api")


urlpatterns = [
    path('',include(auth_api.urls)),

]
