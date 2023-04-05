# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from rest_framework import serializers

# Internal:
from .models import Profile
from tasks.models import Task
from watches.models import Watch
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    tasks_count = serializers.ReadOnlyField()
    watching_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_watching_id(self, obj):
        """
        Check if the logged-in user is watching any taks
        """
        user = self.context['request'].user
        if user.is_authenticated:
            watching = Watches.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            return watching.id if watching else None
        return None

    class Meta:
        model = Profile
        fields = [
            'id',
            'owner',
            'name',
            'job_role',
            'created_on',
            'updated_on',
            'image',
            'is_owner',
            'tasks_count',
            'watching_count',
        ]
