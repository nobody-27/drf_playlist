from Serilizer_Relations.models import Singer,Song
from rest_framework import serializers

#for nested Serializer 
class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id','title','singer','duration']

import json

class SingerSerializer(serializers.ModelSerializer):
    sungby = SongSerializer(many=True,read_only=True)
    class Meta:
        model = Singer
        fields = ['id','name','gender','sungby']

    def to_representation(self, obj):
        data = super(SingerSerializer,self).to_representation(obj)
        dumped_data = json.dumps(data)
        loaded_data = json.loads(dumped_data)
        test = loaded_data['sungby']


        for eact in test:
            print(eact)
            eact['neeraj']= "sameer"
            eact['sesstion_id']="datatadnfkjasndkfakjdf"
            print(eact)

        data['sungby'] = test

        return data














# class SongSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Song
#         fields = ['id','title','singer','duration']

# class SingerSerializer(serializers.ModelSerializer):
#     # song = serializers.StringRelatedField(many=True,read_only=True)
#     # song = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
#     # sungby = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='song-detail')
    
#     class Meta:
#         model = Singer
#         fields = ['id','name','gender','sungby']
