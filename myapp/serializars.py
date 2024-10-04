from rest_framework import serializers
from.models import Person 


class PersonSerializar(serializers.Serializer):

    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
