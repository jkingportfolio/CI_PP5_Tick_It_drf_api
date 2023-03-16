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
            'members',
            'updated_on',
        ]

    def create(self, validated_data):
        """
        Handle possible duplication
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplication'
            })


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
            'members',
            'updated_on',
            'pack'
        ]
