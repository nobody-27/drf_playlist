from django.shortcuts import render
from Token_Authentication.models import Token_Testing
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from Token_Authentication.serializers import *
# Create your views here.


class Testing_Model(viewsets.ModelViewSet):
    queryset = Token_Testing.objects.all()
    serializer_class = TokenAuthentication