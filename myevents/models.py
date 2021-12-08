from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.TextField("Event Name", blank=False)
    location = models.TextField("Location", blank=False)
    time = models.DateTimeField("Event Time", blank=False)

    class Meta:
        verbose_name_plural = "Events"

