from django.db import models
from django.core import serializers


class TimePeriod(models.Model):
    title = models.CharField(max_length=128, default="[Placeholder title]")
    start = models.DateTimeField()


