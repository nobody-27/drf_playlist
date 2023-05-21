from django.shortcuts import render
from rest_framework.response import Response
from function_based.models import NoteBook
from ViewSet.serializers import View_SET_Seriliasers
from rest_framework import status
from rest_framework import viewsets
# Create your views here.


class NoteBookViewSet(viewsets.ViewSet):
    def list(self,request):
        print('****List****')
        print('Basename:',self.basename)
        print('Action:',self.action)
        print('Detail:',self.detail)
        print('Suffix:',self.suffix)
        print('Name:',self.name)
        print('Description:',self.description)


        note = NoteBook.objects.all()
        serializer = View_SET_Seriliasers(note,many=True)
        return Response(serializer.data)
    
    def retrieve(self,request,pk=None):
        print('****Retrive****')
        print('Basename:',self.basename)
        print('Action:',self.action)
        print('Detail:',self.detail)
        print('Suffix:',self.suffix)
        print('Name:',self.name)
        print('Description:',self.description)
        id = pk
        if id is not None:
            note = NoteBook.objects.get(id=id)
            serializer = View_SET_Seriliasers(note)
            return Response(serializer.data)

        
    def create(self,request):
        print('****Create****')
        print('Basename:',self.basename)
        print('Action:',self.action)
        print('Detail:',self.detail)
        print('Suffix:',self.suffix)
        print('Name:',self.name)
        print('Description:',self.description)
        serializer = View_SET_Seriliasers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk):
        print('****Update****')
        print('Basename:',self.basename)
        print('Action:',self.action)
        print('Detail:',self.detail)
        print('Suffix:',self.suffix)
        print('Name:',self.name)
        print('Description:',self.description)
        id = pk
        note = NoteBook.objects.get(id = id)
        serializer = View_SET_Seriliasers(note,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self,request,pk):
        print('****Partial_Update****')
        print('Basename:',self.basename)
        print('Action:',self.action)
        print('Detail:',self.detail)
        print('Suffix:',self.suffix)
        print('Name:',self.name)
        print('Description:',self.description)
        id = pk
        note = NoteBook.objects.get(id = id)
        serializer = View_SET_Seriliasers(note,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Update'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

    def destroy(self,request,pk):
        print('****Destroy_Update****')
        print('Basename:',self.basename)
        print('Action:',self.action)
        print('Detail:',self.detail)
        print('Suffix:',self.suffix)
        print('Name:',self.name)
        print('Description:',self.description)
        id = pk
        note = NoteBook.objects.get(id=id)
        note.delete()
        return Response({'msg':"Data Deleted"})