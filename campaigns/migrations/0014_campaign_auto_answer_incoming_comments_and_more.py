# Generated by Django 5.0.7 on 2024-08-06 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("campaigns", "0013_alter_campaign_interacted_users"),
    ]

    operations = [
        migrations.AddField(
            model_name="campaign",
            name="auto_answer_incoming_comments",
            field=models.CharField(
                choices=[("yes", "Yes"), ("no", "No")], max_length=255, null=True
            ),
        ),
        migrations.AddField(
            model_name="campaign",
            name="blacklisted_keywords",
            field=models.CharField(max_length=2255, null=True),
        ),
        migrations.AddField(
            model_name="campaign",
            name="engagement_goal",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="campaign",
            name="engagment_depth",
            field=models.CharField(
                choices=[
                    ("posts", "Posts"),
                    ("responses", "Responses"),
                    ("both", "Both"),
                ],
                default="posts",
                max_length=255,
            ),
        ),
        migrations.AddField(
            model_name="campaign",
            name="global_activity_timeframe",
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name="campaign",
            name="max_comments_per_week",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="campaign",
            name="max_generated_words_per_comments_comment",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="campaign",
            name="max_generated_words_per_post_comment",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="campaign",
            name="overall_goal",
            field=models.TextField(default="", null=True),
        ),
    ]
