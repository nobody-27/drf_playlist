from django.shortcuts import render
from rest_framework.response import Response
from Model_View_Set_last.models import ClassRoom
from Model_View_Set_last.serializers import ClassRoomSerializer
from rest_framework import status
from rest_framework import viewsets

# Create your views here.


class ClassRoomViewSet(viewsets.ModelViewSet):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomSerializer

import io
#only for read only api
class ClassRoomReadonlyViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = ClassRoomSerializer
    queryset = ClassRoom.objects.all()


    # def get_queryset(self):
    #     data = self.request.query_params
    #     convert_into_dict = dict(self.request.query_params)
    #     print(convert_into_dict,"data")
    #     filter_value = self.request.query_params.get('id',None)
    #     print(filter_value,"This is Filter value")
    #     return ClassRoom.objects.all()
    



    