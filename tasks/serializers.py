# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from rest_framework import serializers

# Internal:
from .models import Task
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TaskSerializer(serializers.ModelSerializer):
    """
    A class for a TaskSerializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    comments_count = serializers.ReadOnlyField()
    created_on = serializers.ReadOnlyField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

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
        ]
