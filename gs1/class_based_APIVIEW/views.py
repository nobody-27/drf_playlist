from django.shortcuts import render
from rest_framework.response import Response
from function_based.serializers import NoteBookSerializers
from function_based.models import NoteBook
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import serializers
# Create your views here.


class NoteBook_API(APIView):
    def get(self,request,pk=None,format=None):
        id = pk
        if id is not None:
            try:
                note = NoteBook.objects.get(id=id)
            except Exception as e:
                raise serializers.ValidationError('Object note Found')
            serializer = NoteBookSerializers(note)
            return Response(serializer.data)
        
        note = NoteBook.objects.all()
        serializer = NoteBookSerializers(note,many=True)
        return Response(serializer.data)
    

    def post(self,request,format=None):
        serializer = NoteBookSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'msg':'Data Created'
            })  
        return Response(serializer.errors)
    

    def put(self,request, pk ,formet=None):
        id = pk
        note = NoteBook.objects.get(id=id)
        serializer = NoteBookSerializers(note,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'msg':'Complete Data Updated'
            })  
        return Response(serializer.errors)
    
    def patch(self,request, pk ,formet=None):
        id = pk
        note = NoteBook.objects.get(id=id)
        serializer = NoteBookSerializers(note,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'msg':'Partial Data Updated'
            })  
        return Response(serializer.errors)
    
    def delete(self,request, pk ,formet=None):
        id = pk
        note = NoteBook.objects.get(id=id)
        note.delete()
        return Response({
            'msg':'Data Deleted'
        })
        


