from Model_View_Set_last.models import ClassRoom
from rest_framework import serializers


class ClassRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = ['id','name','class_url','city']



        