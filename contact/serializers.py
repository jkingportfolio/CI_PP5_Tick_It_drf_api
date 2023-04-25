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
    class Meta:
        model = Contact
        fields = '__all__'
