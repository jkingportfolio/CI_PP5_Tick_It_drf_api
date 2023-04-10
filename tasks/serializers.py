# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from rest_framework import serializers

# Internal:
from .models import Task
from watches.models import Watch
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TaskSerializer(serializers.ModelSerializer):
    """
    A class for a TaskSerializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    comments_count = serializers.ReadOnlyField()
    created_on = serializers.DateField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    watching_id = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_watching_id(self, obj):
        """
        Check if the logged-in user is watching any taks
        """
        user = self.context['request'].user
        if user.is_authenticated:
            watching = Watch.objects.filter(
                owner=user, task=obj
            ).first()
            return watching.id if watching else None
        return None

    class Meta:
        model = Task
        fields = [
            'id',
            'is_owner',
            'owner',
            'created_on',
            'title',
            'task_body',
            'updated_on',
            'priority',
            'due_date',
            'files',
            'assigned_to',
            'completed',
            'pack',
            'comments_count',
            'profile_id',
            'profile_image',
            'watching_id',
        ]
