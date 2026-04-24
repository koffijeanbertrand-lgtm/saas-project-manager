from django.db import models
from django.conf import settings


class Plan(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    max_organizations = models.IntegerField(default=1)
    max_projects = models.IntegerField(default=2)
    max_tasks = models.IntegerField(default=10)
    is_active = models.BooleanField(default=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Subscription(models.Model):

    class Status(models.TextChoices):
        ACTIVE = 'ACTIVE', 'Actif'
        CANCELLED = 'CANCELLED', 'Annulé'
        EXPIRED = 'EXPIRED', 'Expiré'

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='subscription'
    )
    plan = models.ForeignKey(
        Plan,
        on_delete=models.PROTECT,
        related_name='subscriptions'
    )
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.ACTIVE
    )
    started_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.plan}"
# Create your models here.
