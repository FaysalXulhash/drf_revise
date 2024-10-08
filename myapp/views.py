from django.shortcuts import render
from.models import Person 
from .serializars import PersonSerializar
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io 
from django.views.decorators.csrf import csrf_exempt


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


@csrf_exempt
def create_person(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        print('strem:', stream)
        pythondata = JSONParser().parse(stream)
        serializer = PersonSerializar(data = pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'successfully created instance !'}
            js_data = JSONRenderer().render(res)
            return HttpResponse(js_data, content_type = 'application/json')
        json_data = JSONRenderer().render(serializar.errors)
        return HttpResponse(js_data, content_type = 'application/json')
