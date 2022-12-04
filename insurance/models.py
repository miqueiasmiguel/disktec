from django.utils import timezone
from django.db import models


class InsuranceClient(models.Model):
    name = models.CharField(max_length=255, unique=False, null=False)
    phone = models.CharField(max_length=255, null=True)
    date = models.DateField(null=True)
    birth_date = models.DateField(null=True)
    rg = models.CharField(max_length=255, unique=True, null=True)
    cpf = models.CharField(max_length=255, unique=True, null=True)
    address = models.CharField(max_length=255, unique=False, null=True)
    house_number = models.IntegerField(unique=False, null=True)
    district = models.CharField(max_length=255, unique=False, null=True)
    city = models.CharField(max_length=255, unique=False, null=True)
    complement = models.CharField(max_length=255, unique=False, null=True)
    machine = models.CharField(max_length=255, unique=False, null=True)
    model = models.CharField(max_length=255, unique=False, null=True)
    total = models.FloatField(max_length=255, unique=False, null=True)
    installments_value = models.FloatField(max_length=255, unique=False, null=False)
    indemnity = models.FloatField(max_length=255, unique=False, null=True)
    photo = models.ImageField(upload_to="media", null=True)
    expiration_date = models.DateField(null=False)
    last_payment = models.DateField(null=True, default=timezone.now)
    payment_status = models.IntegerField(default=3, null=False)
    obs = models.CharField(max_length=255, unique=False, null=True)

    class Meta:
        ordering = ("machine",)
