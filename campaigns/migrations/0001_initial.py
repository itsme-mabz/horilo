# Generated by Django 5.0.7 on 2024-08-02 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Campaign",
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
                ("name", models.CharField(max_length=255)),
                ("campaign_type", models.CharField(max_length=255)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("active", "Active"),
                            ("paused", "Paused"),
                            ("archived", "Archived"),
                        ],
                        max_length=20,
                    ),
                ),
                ("kpis", models.JSONField()),
                ("start_date", models.DateField()),
                ("end_date", models.DateField(blank=True, null=True)),
                (
                    "priority",
                    models.CharField(
                        choices=[("high", "High"), ("mid", "Mid"), ("low", "Low")],
                        max_length=10,
                    ),
                ),
            ],
        ),
    ]