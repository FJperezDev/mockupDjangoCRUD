from django.shortcuts import render
from ..models import Project
from ..serializers import ProjectSerializer
from rest_framework import viewsets, permissions

# Create your views here.

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.AllowAny]
    