from django.db import models
from django.utils import timezone


class DailyIncome(models.Model):
    name = models.CharField(max_length=255, null=False, unique=False)
    date = models.DateField(null=True, default=timezone.now)
    value = models.FloatField(null=False, unique=False)
    type = models.CharField(max_length=255, null=False, unique=False)
