# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import IntegrityError
from rest_framework import serializers

# Internal:
from .models import Watch
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class WatchSerializer(serializers.ModelSerializer):
    """
    A class for a WatchSerializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Watch
        fields = [
            'id',
            'owner',
            'created_on',
            'task',
        ]

    def create(self, validated_data):
        """
        Function to handle potential duplicates of watches by the same user
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplication'
            })
