from django.db import models


class ServiceClient(models.Model):
    name = models.CharField(max_length=255, unique=False, null=False)
    phone = models.CharField(max_length=255, null=True)
    date = models.DateField(null=True)
    birth_date = models.DateField(null=True)
    rg = models.CharField(max_length=255, unique=False, null=True)
    cpf = models.CharField(max_length=255, unique=False, null=True)
    address = models.CharField(max_length=255, unique=False, null=True)
    house_number = models.IntegerField(unique=False, null=True)
    district = models.CharField(max_length=255, unique=False, null=True)
    city = models.CharField(max_length=255, unique=False, null=True)
    complement = models.CharField(max_length=255, unique=False, null=True)
    photo = models.ImageField(upload_to="media", null=True)
    service_type = models.CharField(max_length=255, unique=False, null=True)
    machine = models.CharField(max_length=255, unique=False, null=True)
    model = models.CharField(max_length=255, unique=False, null=True)
    total = models.FloatField(max_length=255, unique=False, null=False)
    payment = models.CharField(max_length=255, unique=False, null=True)
    payment_status = models.IntegerField(default=3, null=False)
    obs = models.CharField(max_length=255, unique=False, null=True)

    class Meta:
        ordering = ("machine",)
