# Generated by Django 4.0.6 on 2022-10-24 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceclient',
            name='payment_status',
            field=models.IntegerField(default=3),
        ),
    ]
