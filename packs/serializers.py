# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from rest_framework import serializers

# Internal:
from .models import Pack
from tasks.serializers import TaskSerializer
from tasks.models import Task
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class PackSerializer(serializers.ModelSerializer):
    """
    A class for a PackSerializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    tasks = serializers.PrimaryKeyRelatedField(
        queryset=Task.objects.all(), many=True)

    class Meta:
        model = Pack
        fields = [
            'id',
            'is_owner',
            'owner',
            'created_on',
            'title',
            'pack_description',
            'updated_on',
            'tasks',
            'profile_id',
            'profile_image',
        ]

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def create(self, validated_data):
        tasks = validated_data.pop('tasks')
        pack = Pack.objects.create(**validated_data)
        pack.tasks.set(tasks)
        return pack


class PackDetailSerializer(PackSerializer):
    """
    A class for a PackDetail Serializer for the
    Pack model used in Detail view
    """
    pack = serializers.ReadOnlyField(source='pack.id')

    class Meta:
        model = Pack
        fields = [
            'id',
            'is_owner',
            'owner',
            'created_on',
            'title',
            'pack_description',
            'updated_on',
            'pack',
            'tasks',
            'profile_id',
            'profile_image',
        ]
