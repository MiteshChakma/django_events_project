from rest_framework import serializers
from myevents.models import *


class EventSerializer(serializers.ModelSerializer):
    #time = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    class Meta:
        model = Event
        fields = (
            'name',
            'location',
            'time'
        )