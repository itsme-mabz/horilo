# Generated by Django 5.0.7 on 2024-08-06 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "campaigns",
            "0018_rename_comment_threashold_campaign_comment_threshold_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="campaign",
            name="id",
            field=models.CharField(
                default="",
                editable=False,
                max_length=12,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
    ]