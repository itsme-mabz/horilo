# Generated by Django 5.0.7 on 2024-08-06 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("campaigns", "0015_alter_campaign_interacted_users"),
    ]

    operations = [
        migrations.AlterField(
            model_name="interacteduser",
            name="full_name",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="interacteduser",
            name="interaction_date",
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name="interacteduser",
            name="job_position",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="interacteduser",
            name="linkedin_profile_url",
            field=models.URLField(null=True),
        ),
    ]