from rest_framework import serializers
from function_based.models import NoteBook


class NoteBookSerializers(serializers.ModelSerializer):
    class Meta:
        model = NoteBook
        fields = ['id','name','roll','city']