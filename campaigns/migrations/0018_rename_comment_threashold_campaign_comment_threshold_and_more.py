# Generated by Django 5.0.7 on 2024-08-06 10:52

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("campaigns", "0017_alter_campaign_interacted_users"),
    ]

    operations = [
        migrations.RenameField(
            model_name="campaign",
            old_name="comment_threashold",
            new_name="comment_threshold",
        ),
        migrations.RenameField(
            model_name="campaign",
            old_name="engagment_depth",
            new_name="engagement_depth",
        ),
        migrations.AlterField(
            model_name="campaign",
            name="formality_level",
            field=models.CharField(
                choices=[("formal", "Formal"), ("informal", "Informal")],
                max_length=255,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="campaign",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
    ]
