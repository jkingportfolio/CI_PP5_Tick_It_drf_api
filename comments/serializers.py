# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from rest_framework import serializers
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Internal:
from .models import Comment
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class CommentSerializer(serializers.ModelSerializer):
    """
    A class for a CommentSerializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Comment
        fields = [
            'id',
            'is_owner',
            'owner',
            'task',
            'created_on',
            'updated_on',
            'comment_body',
        ]


class CommentDetailSerializer(CommentSerializer):
    """
    A class for a CommentDetail Serializer for the
    Comment model used in Detail view
    """
    task = serializers.ReadOnlyField(source='task.id')
