# Generated by Django 5.1.1 on 2024-11-16 19:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primeraApp', '0008_remove_cita_estado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cita',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='cita',
            name='vehiculo',
        ),
        migrations.AddField(
            model_name='cita',
            name='cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='primeraApp.cliente'),
        ),
        migrations.AddField(
            model_name='cita',
            name='vehiculo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='primeraApp.vehiculo'),
        ),
    ]
