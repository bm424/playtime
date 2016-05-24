from django.http import JsonResponse
from django.shortcuts import render
from django.core import serializers

from .models import TimePeriod


def simplecal(request):
    events = [{'title': t.title, 'start': t.start.strftime("%Y-%m-%dT%H:%M:%S")} for t in TimePeriod.objects.all()]
    return JsonResponse(events, safe=False)


def index(request):
    return render(request, 'index.html')
