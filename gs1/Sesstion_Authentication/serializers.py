from rest_framework import serializers
from Sesstion_Authentication.models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id','name','roll','bio']

