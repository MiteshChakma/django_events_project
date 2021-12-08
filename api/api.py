from django.conf.urls import url

# importing feed views
from myevents.views import *

from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    url(r'^events/$', event, name="event"),
    url(r'^events/(?P<id>.+)/$', event_ref),
]