from rest_framework import serializers
from.models import Person 


class PersonSerializar(serializers.Serializer):

    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()

    def create(self, validated_data):
        return Person.objects.create(**validated_data)
