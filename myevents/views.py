from django.shortcuts import render
from myevents.models import *
from myevents.serializers import *
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, parser_classes

from django.conf import settings
from EventsProject import settings
# Create your views here.


# HTTP method POST for creating event record

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
@parser_classes([FormParser, MultiPartParser])
def event(request):
    '''
        GET list of events, POST a new event, DELETE events by id
        :param request:
        :param id:
        :return:
    '''
    if request.method == 'POST':
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        data = Event.objects.objects.all()
        serializer = EventSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((permissions.AllowAny,))
@parser_classes([FormParser, MultiPartParser])
def event_ref(request, id):
    '''
    find tutorial by id
    GET / PUT / DELETE events
    :param request:
    :param id:
    :return:
    '''
    try:
        data = Event.objects.get(id=id)
    except Event.DoesNotExist:
        return Response({'message': 'The Event does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        print("Get")
        serializer = EventSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        print("Delete")
        data = Event.objects.get(id=id)
        data.delete()
        data.save()
        return Response("Event deleted", status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        event_data = request.data
        serializer = EventSerializer(data, data=event_data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)









