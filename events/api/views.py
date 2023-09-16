from django.shortcuts import render
from rest_framework import viewsets
from ..models import Event
from .serializers import EventModelSerializer

# Create your views here.
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by("-id")
    serializer_class = EventModelSerializer
 
