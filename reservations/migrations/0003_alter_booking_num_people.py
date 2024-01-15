# Generated by Django 5.0.1 on 2024-01-15 17:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("reservations", "0002_booking_num_people"),
    ]

    operations = [
        migrations.AlterField(
            model_name="booking",
            name="num_people",
            field=models.PositiveIntegerField(
                default=1,
                help_text="Number of people attending",
                validators=[django.core.validators.MaxValueValidator(limit_value=10)],
            ),
        ),
    ]
