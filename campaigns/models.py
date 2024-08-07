from django.db import models
import uuid
from django.conf import global_settings

AUTH_USER_MODEL = 'accounts.User'

class InteractedUser(models.Model):
    full_name = models.CharField(max_length=255, null=True)
    interaction_date = models.DateTimeField(null=True)
    job_position = models.CharField(max_length=255, null=True)
    linkedin_profile_url = models.URLField(null=True)

    def __str__(self):
        return self.full_name

class Campaign(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('paused', 'Paused'),
        ('archived', 'Archived'),
    ]

    PRIORITY_CHOICES = [
        ('high', 'High'),
        ('mid', 'Mid'),
        ('low', 'Low'),
    ]

    CAMPAIGN_TYPE = [
        ('profile_stalker', 'Profile Stalker'),
        ('content_finder', 'Content Finder'),
        ('profile_finder', 'Profile Finder'),
        ('targeted_commentor', 'Targeted Commentor')
    ]

    id = models.CharField(max_length=12, unique=True, editable=False, default='' , primary_key=True)
    name = models.CharField(max_length=255, null=True)
    campaign_type = models.CharField(max_length=255, choices=CAMPAIGN_TYPE, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True, blank=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, null=True)
    interacted_users = models.ManyToManyField(InteractedUser, related_name='campaigns', blank=True)
    progress = models.JSONField(null=True) 
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='campaigns', null=True)

    B_FIELDS = [
        ('yes', 'Yes'),
        ('no', 'No')
    ]

    

    FORMALITY_LEVELS = [
        ('formal', 'Formal'),
        ('informal', 'Informal') 
    ]
    
    ENGAGEMENT_DEPTH = [
        ('posts', 'Posts'),
        ('responses', 'Responses'),
        ('both', 'Both')
    ]

    gSheet_input = models.FileField(upload_to='gsheets/', null=True)
    use_emoji = models.CharField(max_length=255, choices=B_FIELDS, null=True)
    hashtags = models.CharField(max_length=255, choices=B_FIELDS, null=True)
    tonality = models.TextField(null=True)
    target_language = models.CharField(max_length=255, choices=global_settings.LANGUAGES, null=True)
    manual_approval = models.CharField(max_length=255, choices=B_FIELDS, null=True)
    formality_level = models.CharField(max_length=255, choices=FORMALITY_LEVELS, null=True)
    comment_threshold = models.IntegerField(null=True)
    published_date_threashhold = models.IntegerField(null=True)  
    max_generated_words_per_post_comment = models.IntegerField(null=True)
    max_generated_words_per_comments_comment = models.IntegerField(null=True)
    auto_answer_incoming_comments = models.CharField(max_length=255, choices=B_FIELDS, null=True)
    max_comments_per_week = models.IntegerField(null=True)
    question_frequency = models.IntegerField(null=True)
    engagement_goal = models.IntegerField(null=True)
    global_activity_timeframe = models.DateTimeField(null=True)  
    engagement_depth = models.CharField(max_length=255, choices=ENGAGEMENT_DEPTH, default='posts')  
    blacklisted_keywords = models.CharField(max_length=2255, null=True)
    overall_goal = models.TextField(null=True, default='')

    def save(self, *args, **kwargs):
        self.update_progress()
        super().save(*args, **kwargs)

    def update_progress(self):
        if not self.user:
            return
        tier_limits = {
            'free': 10,
            'standard': 20,
            'premium': 50
        }
        max_interacted_users = tier_limits.get(self.user.tier_type, 10)
        current_interacted_users_count = self.interacted_users.count()
        self.progress = {
            'percentage': (current_interacted_users_count / max_interacted_users) * 100
        }

    def calculate_progress_bar(self):
        total_actions = self.progress.get('total_actions', 0)
        monthly_budget = self.progress.get('monthly_budget', 0)
        if monthly_budget > 0:
            return (total_actions / monthly_budget) * 100
        return 0

    def budget_warning(self):
        if self.calculate_progress_bar() >= 80:
            return "You will run out of budget soon. To ensure consistent action, please upgrade your plan [link to billing page]."
        return None

    def __str__(self):
        return self.name
