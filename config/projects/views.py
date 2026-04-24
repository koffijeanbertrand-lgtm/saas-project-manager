from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from .models import Project
from .serializers import ProjectSerializer
from subscriptions.utils import can_create_project


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        if not can_create_project(self.request.user):
            raise PermissionDenied("Limite de projets atteinte pour votre plan.")
        serializer.save(owner=self.request.user)
# Create your views here.
