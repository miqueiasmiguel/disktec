from django.db import models
from django.utils import timezone


class Note(models.Model):
    content = models.TextField(null=False, unique=False)
    date = models.DateField(null=True, default=timezone.now)
