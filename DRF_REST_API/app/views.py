
from functools import partial
from urllib import response
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import StudentModel
from .serlializers import StudentSerialzers

@api_view(['GET'])
def Overview(request):

    about = {
        "Topic":"REST APIs and HTTP Methods",
        "By":"Scaler Topics",
        "Content":[
            'Overview',
            'Scope',
            'What is a REST API?',
            'What is Django Rest Framework?',
            'How to Create a basic API using Django Rest Framework ?',
            'Essential HTTP methods in RESTful API development',
            'Conclusion'
        ]
    }

    return Response(about)


@api_view(['POST'])
def addStudent(request):

    # Receive the data from the client side
    dataReceived = request.data
    studentData = StudentSerialzers(data=dataReceived)

    # Check if data already exist or not
    if StudentModel.objects.filter(**dataReceived).exists():
        return Response(status=status.HTTP_403_FORBIDDEN)

    # Validate the data entered by the user
    if studentData.is_valid():
        studentData.save()
        return Response(studentData.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update(request, pk):
    student = StudentModel.objects.get(pk=pk)
    studentData = StudentSerialzers(instance=student, data=request.data)

    if studentData.is_valid():
        studentData.save()
        return Response(studentData.data)

    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PATCH'])
def modify(request, pk):
    student = StudentModel.objects.get(pk=pk)
    studentData = StudentSerialzers(instance=student, data=request.data, partial=True)

    if studentData.is_valid():
        studentData.save()
        return Response(studentData.data)

    else:
        return Response(status=status.HTTP_404_NOT_FOUND)