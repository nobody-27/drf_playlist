from django.shortcuts import render
from function_based.models import NoteBook
from GENERIC_API_VIEW.serializer import GENERIC_API_VIEW_DATA

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
# Create your views here.

class NoteBook_API(GenericAPIView,ListModelMixin):
    queryset = NoteBook.objects.all()
    serializer_class = GENERIC_API_VIEW_DATA

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    

class NoteBook_CREATE(GenericAPIView,CreateModelMixin):
    queryset = NoteBook.objects.all()
    serializer_class = GENERIC_API_VIEW_DATA

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


class NoteBook_Retrieve(GenericAPIView,RetrieveModelMixin):
    queryset = NoteBook.objects.all()
    serializer_class = GENERIC_API_VIEW_DATA

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

class NoteBook_UPDATE(GenericAPIView,UpdateModelMixin):
    queryset = NoteBook.objects.all()
    serializer_class = GENERIC_API_VIEW_DATA

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)


class NoteBook_Destroy(GenericAPIView,DestroyModelMixin):
    queryset = NoteBook.objects.all()
    serializer_class = GENERIC_API_VIEW_DATA

    def delete(self,request,*args,**kwargs):
        print(request.method)
        print(kwargs)
        print(request.body)
        return self.destroy(request,*args,**kwargs)
    

