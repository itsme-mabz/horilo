from rest_framework import serializers
from .models import Campaign

class CampaignSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username') 

    class Meta:
        model = Campaign
        fields = ['id', 'name', 'campaign_type', 'status', 'kpis', 'start_date', 'end_date', 'priority', 'user']
