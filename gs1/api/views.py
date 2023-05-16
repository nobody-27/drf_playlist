from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import ParseError
from django.http import HttpResponse
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
def student_detail(request):
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = ParseError(json_data)

        seriliser = StudentSerializer(python_data)
        if seriliser.is_valid():
            seriliser.save()
            res = {'msg':"data"}
            return HttpResponse(res,content_type = 'application/json')
