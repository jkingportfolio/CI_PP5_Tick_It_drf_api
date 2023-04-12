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
    REASON_CHOICES = [
        ('LOGIN', 'Login issue'),
        ('REPORT_POST', 'Report a post'),
        ('GENERAL', 'General Enquiry'),
        ('DELETE_ACCOUNT', 'Delete Account'),
    ]

    reason = models.CharField(
        max_length=255,
        choices=REASON_CHOICES,
        default='GENERAL'
    )
    name = models.CharField(
        max_length=50,
        blank=False, null=False
    )
    email = models.EmailField(
        max_length=70,
        blank=False, null=False
    )
    message = models.TextField(
        max_length=500,
        blank=False, null=False
    )
    message_date = models.DateTimeField(
        auto_now=True,
        blank=False, null=False
    )

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        """
        Returns contact name and date as a string
        """
        return f'Message from {self.name} on {self.message_date}'
