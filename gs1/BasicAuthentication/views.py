from django.shortcuts import render
from Model_View_Set_last.models import ClassRoom
from Model_View_Set_last.serializers import ClassRoomSerializer
from rest_framework import viewsets

from rest_framework.authentication import BasicAuthentication

from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
# Create your views here.



class Api_for_Authentication(viewsets.ModelViewSet):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomSerializer

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]



