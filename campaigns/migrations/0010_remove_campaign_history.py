# Generated by Django 5.0.7 on 2024-08-06 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("campaigns", "0009_remove_campaign_settings"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="campaign",
            name="history",
        ),
    ]
