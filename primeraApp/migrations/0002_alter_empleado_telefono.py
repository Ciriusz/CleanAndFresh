# Generated by Django 5.1.1 on 2024-11-07 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primeraApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='telefono',
            field=models.BigIntegerField(),
        ),
    ]
