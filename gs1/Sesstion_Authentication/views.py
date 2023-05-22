from django.shortcuts import render
from Sesstion_Authentication.serializers import PersonSerializer
from rest_framework import viewsets
from Sesstion_Authentication.models import Person
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoObjectPermissions
# Create your views here.

#session Authetication
class PersonModelViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    authentication_classes = [SessionAuthentication]
    # permission_classes=[AllowAny]
    # permission_classes = [IsAdminUser]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticatedOrReadOnly] 
    permission_classes = [DjangoModelPermissions]





 





    





