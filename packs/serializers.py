# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from rest_framework import serializers

# Internal:
from .models import Pack
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class PackSerializer(serializers.ModelSerializer):
    """
    A class for a PackSerializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

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

    # def create(self, validated_data):
    #     tasks_data = validated_data.pop('tasks')
    #     pack = Pack.objects.create(**validated_data)

    #     for task_data in tasks_data:
    #         task, _ = Task.objects.get(id=task_data['id'])
    #         pack.tasks.add(task)

    #     return pack

    def create(self, serializer):
        tasks = json.loads(self.request.data.get('tasks')) # Deserialize list from JSON string
        serializer.save(user=self.request.user, tasks=tasks)


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
