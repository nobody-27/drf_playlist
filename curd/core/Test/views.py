from django.shortcuts import render
import io
from .models import Student
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .serializers import StudentSerializer
from django.http import HttpResponse

# Create your views here.

def student_api(request):
    if request.method == "GET":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id',None)
        if id is not None:
            stu = Student.objects.filter(id=id)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        
        stu = Student.objects.all()
        serializer = StudentSerializer(stu,many=True)
        return HttpResponse(serializer.data,content_type='application/json')



