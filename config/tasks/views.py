from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from .models import Task
from .serializers import TaskSerializer
from subscriptions.utils import can_create_task


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(project__owner=self.request.user)

    def perform_create(self, serializer):
        project = serializer.validated_data.get('project')
        if not can_create_task(self.request.user, project):
            raise PermissionDenied("Limite de tâches atteinte pour votre plan.")
        serializer.save()
# Create your views here.
