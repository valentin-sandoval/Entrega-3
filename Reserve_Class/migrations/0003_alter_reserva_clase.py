# Generated by Django 5.0.3 on 2024-04-13 19:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Reserve_Class", "0002_clase_delete_registro_remove_reserva_nivel_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reserva",
            name="clase",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reservas",
                to="Reserve_Class.clase",
            ),
        ),
    ]
