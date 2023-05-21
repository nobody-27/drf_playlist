from django.shortcuts import render
from function_based.models import NoteBook
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView
from function_based.serializers import NoteBookSerializers
# Create your views here.

class Concrete_Notebook_list(ListAPIView):
    queryset = NoteBook.objects.all()
    serializer_class = NoteBookSerializers


class Concrete_Notebook_Create(CreateAPIView):
    queryset = NoteBook.objects.all()
    serializer_class = NoteBookSerializers


class Concrete_Notebook_Retrieve(RetrieveAPIView):
    queryset = NoteBook.objects.all()
    serializer_class = NoteBookSerializers

class Concrete_Notebook_Update(UpdateAPIView):
    queryset = NoteBook.objects.all()
    serializer_class = NoteBookSerializers



class Concrete_Notebook_Destroy(DestroyAPIView):
    queryset = NoteBook.objects.all()
    serializer_class = NoteBookSerializers



#mixin class start
class Concrete_List_Create(ListCreateAPIView):
    queryset = NoteBook.objects.all()
    serializer_class = NoteBookSerializers



class Concrete_Retrive_Update(RetrieveUpdateAPIView):
    queryset = NoteBook.objects.all()
    serializer_class = NoteBookSerializers


class Concrete_Retrive_Destroy(RetrieveDestroyAPIView):
    queryset = NoteBook.objects.all()
    serializer_class = NoteBookSerializers

