# Generated by Django 5.0.7 on 2024-08-06 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "campaigns",
            "0003_interacteduser_campaign_history_campaign_progress_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="campaign",
            name="campaign_id",
            field=models.CharField(
                default="", editable=False, max_length=12, unique=True
            ),
        ),
    ]
