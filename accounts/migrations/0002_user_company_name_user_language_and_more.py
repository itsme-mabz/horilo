# Generated by Django 5.0.7 on 2024-08-01 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="company_name",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="language",
            field=models.CharField(default="en", max_length=50),
        ),
        migrations.AddField(
            model_name="user",
            name="newsletter_opt_in",
            field=models.BooleanField(default=True),
        ),
    ]
