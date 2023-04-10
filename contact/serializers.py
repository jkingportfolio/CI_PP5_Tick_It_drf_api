# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from rest_framework import serializers

# Internal:
from .models import Contact
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class ContactSerializer(serializers.ModelSerializer):
    """
    A class for a ContactSerializer
    """
    reason = serializers.ReadOnlyField()
    name = serializers.ReadOnlyField()
    email = serializers.ReadOnlyField()
    message = serializers.ReadOnlyField()


    class Meta:
        model = Contact
        fields = [
            'id',
            'reason'
            'name',
            'email',
            'message',
            'message_date',
        ]
