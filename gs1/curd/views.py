from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from curd.models import Student
# from curd.serializers import StudentSerializer_Curd
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

# @csrf_exempt
# def student_api_curd(request):
#     if request.method == "GET":
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         id = python_data.get('id',None)
#         if id  is not None:
#             stu = Student.objects.get(id=id)
#             serilizer = StudentSerializer_Curd(stu)
#             json_data = JSONRenderer().render(serilizer.data)
#             return HttpResponse(json_data,content_type ='application/json')
        
#         stu = Student.objects.all()
#         serilizer = StudentSerializer_Curd(stu,many=True)
#         json_data = JSONRenderer().render(serilizer.data)
#         return HttpResponse(json_data,content_type ='application/json')
    
#     if request.method == 'POST':
#         json_data = request.body
#         strame = io.BytesIO(json_data)
#         python_data = JSONParser().parse(strame)
#         serilizer = StudentSerializer_Curd(data=python_data)
#         if serilizer.is_valid():
#             serilizer.save()
#             res = {'msg':'Data created','data':serilizer.data}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data,content_type ='application/json')
        
#         json_data = JSONRenderer().render(serilizer.errors)
#         return HttpResponse(json_data,content_type ='application/json')
    
#     if request.method == 'PUT':
#         json_data = request.body
#         strame = io.BytesIO(json_data)
#         python_data = JSONParser().parse(strame)
#         id = python_data.get('id')
#         stu = Student.objects.get(id=id)
#         serilizer = StudentSerializer_Curd(stu,data=python_data,partial=True)
#         if serilizer.is_valid():
#             serilizer.save()
#             res = {'msg':'Data Update'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data,content_type ='application/json')
#         json_data = JSONRenderer().render(serilizer.errors)
#         return HttpResponse(json_data,content_type ='application/json')
    
#     if request.method == "DELETE":
#         json_data = request.body
#         strame = io.BytesIO(json_data)
#         python_data = JSONParser().parse(strame)
#         id = python_data.get('id')
#         stu = Student.objects.get(id=id)
#         stu.delete()
#         res = {
#             'msg':"data Delete"
#         }
#         json_data = JSONRenderer().render(res)
#         return  HttpResponse(json_data,content_type ='application/json' )







