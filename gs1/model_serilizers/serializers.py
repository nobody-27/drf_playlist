from rest_framework import serializers
from curd.models import Student

class StudentSerilizer(serializers.ModelSerializer):

    fields = ['name','roll','city']
    

    class Meta:
        model = Student
