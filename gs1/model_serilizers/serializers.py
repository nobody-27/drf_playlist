from rest_framework import serializers
from curd.models import Student

class StudentSerilizer(serializers.ModelSerializer):
    # name = serializers.CharField(read_only=True) #if you don't want to update your any filed then
    #make it name (read_only=True)

    class Meta:
        model = Student
        fields = ['name','roll','city']
        # extra_kwargs = {'name':{'read_only':True}}

    #field level Validation
    def validate_roll(self,value):
        if value != 100:
            raise serializers.ValidationError("in valid input")
        return value
    
    #obj level Validation
    def validate(self,data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'rohi' and ct.lower() != 'ranchi':
            raise serializers.ValidationError('City Must be Rachit')
        return data

        



    
    




    
