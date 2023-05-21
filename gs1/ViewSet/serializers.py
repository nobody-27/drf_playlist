from rest_framework import serializers
from function_based.models import NoteBook


class View_SET_Seriliasers(serializers.ModelSerializer):
    class Meta:
        model = NoteBook
        fields = ['id','name','roll','city']