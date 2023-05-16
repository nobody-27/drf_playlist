from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
# Create your views here.

def student_detail(request):
    stu = Student.objects.get(id =1 )
    print(stu.data,"stu data")
    serialzer = StudentSerializer(stu)
    print(serialzer.data,"data")
    json_data = JSONRenderer().render(serialzer.data)
    return HttpResponse(json_data,content_type = 'application/json')

