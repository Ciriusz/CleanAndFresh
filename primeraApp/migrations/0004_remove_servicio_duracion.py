# Generated by Django 5.1.1 on 2024-11-15 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('primeraApp', '0003_cliente_apellido_alter_cliente_telefono'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicio',
            name='duracion',
        ),
    ]
