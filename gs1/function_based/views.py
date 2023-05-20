from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from function_based.serializers import NoteBookSerializers
from function_based.models import NoteBook
# Create your views here.


#for testing
@api_view(['POST','GET'])
def hello_world(request):
    if request.method == "GET":
        print(request.data)
        return Response({"msg": "GET REQUEST"})
    if request.method == "POST":
        print(request.data)
        name = request.data.get('name')
        print(name)
        return Response({"msg":"POST REQUEST","data":request.data})
    



@api_view(['GET','POST','PUT','DELETE'])
def notebook_api(request):
    if request.method == "GET":
        id = request.data.get('id')
        if id is not None:
            note = NoteBook.objects.get(id=id)
            serilizer = NoteBookSerializers(note)
            return Response(serilizer.data)

        note = NoteBook.objects.all()
        serilizer = NoteBookSerializers(note,many=True)
        return Response(serilizer.data)

    if request.method == "POST":
        # print(type(request.data),"types")
        serilizer = NoteBookSerializers(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'Data Created'})
        return Response(serilizer.errors)    
    
    if request.method == "PUT":
        id = request.data.get('id',None)
        note = NoteBook.objects.get(id=id)
        serilizer =  NoteBookSerializers(note,data=request.data,partial=True)

        if serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'Data Updated'})
        
        return Response(serilizer.errors)
    
    if request.method == "DELETE":
        id = request.data.get('id',None)
        note = NoteBook.objects.get(id=id).delete()
        return Response({'msg':'Object Deleted'})



