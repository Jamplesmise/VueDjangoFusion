from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)