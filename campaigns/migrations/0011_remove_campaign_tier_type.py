# Generated by Django 5.0.7 on 2024-08-06 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("campaigns", "0010_remove_campaign_history"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="campaign",
            name="tier_type",
        ),
    ]
