from django.shortcuts import render
from Serilizer_Relations.serializers import SongSerializer,SingerSerializer
from rest_framework import viewsets
from rest_framework.generics import GenericAPIView
from Serilizer_Relations.models import Singer,Song
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class SongApiView(GenericAPIView):
    serializer_class = SongSerializer
    queryset = Song.objects.all()

    def get(self, request):
        data = Song.objects.all()
        serializer = SongSerializer(data,many=True)
        return Response({"status": "success", "message": "KOT Order list","data": serializer.data,"code": status.HTTP_200_OK})


class SingerApiView(GenericAPIView):
    serializer_class = SingerSerializer
    queryset = Singer.objects.all()

    def get_object(self, singer_id):
        singer_obj = get_object_or_404(Singer, id=singer_id)
        return singer_obj

    def get(self,request,singer_id):
        print(singer_id,"id")
        # data = Singer.objects.all()
        singer = self.get_object(singer_id)
        serializer = self.serializer_class(singer)

        return Response({"status": "success", "message": "List Of Singer list","data": serializer.data,"code": status.HTTP_200_OK})


# class SingerViewset(viewsets.ModelViewSet):
#     queryset = Singer.objects.all()
#     serializer_class = SingerSerializer()

# class SongViewset(viewsets.ModelViewSet):
#     queryset = Song.objects.all()
#     serializer_class = SongSerializer()

