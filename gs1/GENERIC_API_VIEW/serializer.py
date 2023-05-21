from rest_framework import serializers
from function_based.models import NoteBook


class GENERIC_API_VIEW_DATA(serializers.ModelSerializer):
    class Meta:
        model = NoteBook
        fields = ['id','name','roll','city']