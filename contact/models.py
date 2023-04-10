"""
A module for models in the contact app
"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd Party
from django.db import models
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Contact(models.Model):
    """
    A class for the contact model
    """
    class Reason(models.TextChoices):
        """
        Contact reason options
        """
        LOGIN = "1", "Login issue"
        REPORT_POST = "2", "Report a post"
        GENERAL = "3", "General Enquiry"
        DELETE_ACCOUNT = "4", "Delete Account"

    reason = models.CharField(
        max_length=2,
        choices=Reason.choices,
        default=Reason.GENERAL
    )
    name = models.CharField(
        max_length=50
        )
    email = models.EmailField(
        max_length=70
        )
    message = models.TextField(
        max_length=500
        )
    message_date = models.DateTimeField(
        auto_now=True
        )

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        """
        Returns contact name and date as a string
        """
        return f'Message from {self.name} on {self.message_date}'