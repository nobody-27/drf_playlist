from rest_framework import serializers
from Token_Authentication.models import Token_Testing


class Token_Testing_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Token_Testing
        fields = ['id','name','roll','description']

