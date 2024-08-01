# Generated by Django 5.0.7 on 2024-08-01 15:19

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_user_company_name_user_language_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="language",
            field=models.CharField(
                choices=[
                    ("en", "English"),
                    ("es", "Spanish"),
                    ("fr", "French"),
                    ("de", "German"),
                    ("zh", "Chinese"),
                ],
                default="en",
                max_length=50,
            ),
        ),
        migrations.CreateModel(
            name="Address",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("country", models.CharField(max_length=100)),
                ("city", models.CharField(max_length=100)),
                ("street", models.CharField(max_length=255)),
                ("house_number", models.CharField(max_length=50)),
                ("zip_code", models.CharField(max_length=20)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="address",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="GlobalActivityTimeframe",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "timezone",
                    models.CharField(
                        default=django.utils.timezone.get_default_timezone_name,
                        max_length=50,
                    ),
                ),
                ("monday_start", models.TimeField(default="08:00")),
                ("monday_end", models.TimeField(default="18:00")),
                ("tuesday_start", models.TimeField(default="08:00")),
                ("tuesday_end", models.TimeField(default="18:00")),
                ("wednesday_start", models.TimeField(default="08:00")),
                ("wednesday_end", models.TimeField(default="18:00")),
                ("thursday_start", models.TimeField(default="08:00")),
                ("thursday_end", models.TimeField(default="18:00")),
                ("friday_start", models.TimeField(default="08:00")),
                ("friday_end", models.TimeField(default="18:00")),
                ("saturday_start", models.TimeField(blank=True, null=True)),
                ("saturday_end", models.TimeField(blank=True, null=True)),
                ("sunday_start", models.TimeField(blank=True, null=True)),
                ("sunday_end", models.TimeField(blank=True, null=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="activity_timeframe",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
