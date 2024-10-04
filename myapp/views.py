from django.shortcuts import render
from.models import Person 
from .serializars import PersonSerializar
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer

def index(request):
    data = Person.objects.all()
    serializar = PersonSerializar(data, many=True)
    json_data = JSONRenderer().render(serializar.data)

    return HttpResponse(json_data)

def details(request, pk):
    data = Person.objects.get(pk=pk)
    serializar = PersonSerializar(data)
    json_data = JSONRenderer().render(serializar.data)

    return HttpResponse(json_data)
