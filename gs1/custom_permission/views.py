from django.shortcuts import render
from Sesstion_Authentication.models import Person
from Sesstion_Authentication.serializers import PersonSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions
from rest_framework import viewsets
from .custom_permisson import Mypermission

# Create your views here.

class Person_list_api(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [Mypermission]

    



