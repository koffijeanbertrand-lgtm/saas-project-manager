from django.db import models
from django.conf import settings
from projects.models import Project


class Task(models.Model):

    class Status(models.TextChoices):
        TODO = 'TODO', 'À faire'
        DOING = 'DOING', 'En cours'
        DONE = 'DONE', 'Terminé'

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.TODO
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='tasks'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Create your models here.
