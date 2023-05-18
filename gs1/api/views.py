from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

# def student_detail(request):
#     stu = Student.objects.get(id =1 )
#     print(stu.data,"stu data")
#     serialzer = StudentSerializer(stu)
#     print(serialzer.data,"data")
#     json_data = JSONRenderer().render(serialzer.data)
#     return HttpResponse(json_data,content_type = 'application/json')


import io
#post
@csrf_exempt
def student_create(request):
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        seriliser = StudentSerializer(data = python_data)
        if seriliser.is_valid():
            seriliser.save()
            res = {'msg':"data"}
            json_data = JSONRenderer().render(res)
            return HttpResponse(seriliser.data,content_type = 'application/json')
        json_data = JSONRenderer().render(seriliser.errors)
        return HttpResponse(json_data,content='application/json')