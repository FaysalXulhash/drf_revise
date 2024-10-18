from django.shortcuts import render
from.models import Person 
from .serializars import PersonSerializer
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io 
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from rest_framework import viewsets

#view sets 
class PersonApi(viewsets.ViewSet):
    def list(self, request):
        person = Person.objects.all()
        serializer = PersonSerializer(person, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk):
        person = Person.objects.get(id=pk)
        serializer = PersonSerializer(person)
        return Response(serializer.data) 
    
    def create(self, request):
        serializer = PersonSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk):
        person = Person.objects.get(id=pk)
        serializer = PersonSerializer(person, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#concrete api view......
# class personapi(ListCreateAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer 

# class person_details_api(RetrieveUpdateDestroyAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer 

# class based api view ...................
# class Personapi(APIView):
#     def get(self, request, format=None):
#         persons = Person.objects.all()
#         serializer = PersonSerializer(persons, many=True)
#         return Response(serializer.data)
#     def post(self, request, format=None):
#         serializer = PersonSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# class person_detail_api(APIView):

#     def get(self, request, pk, format=None):
#         person = Person.objects.get(id=pk)
#         serializer = PersonSerializer(person)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         person = Person.objects.get(id=pk)
#         serializer = PersonSerializer(person, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def patch(self, request, pk, format=None):
#         person = Person.objects.get(id=pk)
#         serializer = PersonSerializer(person, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         person = Person.objects.get(id=pk)
#         person.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# #function based api view................
# @api_view(['GET', 'POST'])
# def personapi(request):
#     if request.method == 'GET':
#         persons = Person.objects.all()
#         serializer = PersonSerializer(persons, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = PersonSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
# def person_detail_api(request, pk):
#     try:
#         person = Person.objects.get(id=pk)
#     except Person.DoesNotExist:
#         return Response(status = status.HTTP_404_NOT_FOUND)

    # if request.method == 'GET':
    #     serializer = PersonSerializer(person)
    #     return Response(serializer.data)
    
    # elif request.method == 'PUT':
    #     serializer = PersonSerializer(person, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # elif request.method == 'PATCH':
    #     serializer = PersonSerializer(person, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # elif request.method == 'DELETE':
    #     person.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

# def index(request):
#     data = Person.objects.all()
#     serializar = PersonSerializar(data, many=True)
#     json_data = JSONRenderer().render(serializar.data)

#     return HttpResponse(json_data, content_type = 'application/json')

# def details(request, pk):
#     data = Person.objects.get(pk=pk)
#     serializar = PersonSerializar(data)
#     json_data = JSONRenderer().render(serializar.data)

#     return HttpResponse(json_data, content_type = 'application/json')


# @csrf_exempt
# def person_api(request):
#     if request.method == 'POST':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         print('strem:', stream)
#         pythondata = JSONParser().parse(stream)
#         serializer = PersonSerializar(data = pythondata)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': 'successfully created instance !'}
#             js_data = JSONRenderer().render(res)
#             return HttpResponse(js_data, content_type = 'application/json')
#         json_data = JSONRenderer().render(serializar.errors)
#         return HttpResponse(js_data, content_type = 'application/json')
    
#     #update person
#     if request.method == 'PUT':
#         json_data = request.body 
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id')
#         person = Person.objects.get(id=id)
#         serializer = PersonSerializar(person, data = pythondata, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': f'successfully updated person - {id}!'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application/json')

#     # delete person
#     if request.method == 'DELETE':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id')
#         person = Person.objects.get(id=id)
#         person.delete()
#         res = {'msg': f'successfully deleted person - {id}!'}
#         json_data = JSONRenderer().render(res)
#         return HttpResponse(json_data, content_type='application/json')
