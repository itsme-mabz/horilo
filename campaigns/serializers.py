from rest_framework import serializers
from .models import Campaign, InteractedUser

class InteractedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = InteractedUser
        fields = ['id', 'full_name', 'interaction_date', 'job_position', 'linkedin_profile_url']

class CampaignSerializer(serializers.ModelSerializer):
    interacted_users = InteractedUserSerializer(many=True)

    class Meta:
        model = Campaign
        fields = '__all__'

    def update(self, instance, validated_data):
        interacted_users_data = validated_data.pop('interacted_users', [])
        
        # Update Campaign fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Handle InteractedUsers update
        interacted_users = []
        for interacted_user_data in interacted_users_data:
            user_id = interacted_user_data.get('id')
            if user_id:
                # Update existing interacted_user
                interacted_user = InteractedUser.objects.get(id=user_id)
                for attr, value in interacted_user_data.items():
                    setattr(interacted_user, attr, value)
                interacted_user.save()
            else:
                # Create new interacted_user
                interacted_user = InteractedUser.objects.create(**interacted_user_data)
            interacted_users.append(interacted_user)

        # Update the many-to-many relationship
        instance.interacted_users.set(interacted_users)
        
        return instance

# from rest_framework import serializers
# from .models import Campaign, InteractedUser

# class InteractedUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = InteractedUser
#         fields = ['id', 'full_name', 'interaction_date', 'job_position', 'linkedin_profile_url']

# class CampaignSerializer(serializers.ModelSerializer):
#     interacted_users = InteractedUserSerializer(many=True)

#     class Meta:
#         model = Campaign
#         # fields = ['id', 'name', 'campaign_type', 'status', 'start_date', 'end_date', 'priority', 'interacted_users', 'progress']
#         fields = '__all__'

#     def update(self, instance, validated_data):
#         # Update the fields on the instance
#         instance.name = validated_data.get('name', instance.name)
#         instance.campaign_type = validated_data.get('campaign_type', instance.campaign_type)
#         instance.status = validated_data.get('status', instance.status)
#         instance.start_date = validated_data.get('start_date', instance.start_date)
#         instance.end_date = validated_data.get('end_date', instance.end_date)
#         instance.priority = validated_data.get('priority', instance.priority)
#         instance.progress = validated_data.get('progress', instance.progress)
#         instance.save()

#         # Handle interacted_users
#         interacted_users_data = validated_data.pop('interacted_users', [])
#         for interacted_user_data in interacted_users_data:
#             user_id = interacted_user_data.get('id')
#             if user_id:
#                 # Update existing interacted_user
#                 interacted_user = InteractedUser.objects.get(id=user_id)
#                 for attr, value in interacted_user_data.items():
#                     setattr(interacted_user, attr, value)
#                 interacted_user.save()
#             else:
#                 # Create new interacted_user
#                 InteractedUser.objects.create(**interacted_user_data)

#         return instance
