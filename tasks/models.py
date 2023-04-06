# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models
from django.contrib.auth.models import User

# Internal:
from packs.models import Pack
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Task(models.Model):
    """
    A class for the task model
    """
    PRIORITY_CHOICES = [
        ('HIGH', 'High'),
        ('MEDIUM', 'Medium'),
        ('LOW', 'Low'),
    ]

    COMPLETION_STATUS = [
        ('NO', 'No'),
        ('IN-PROGRESS', 'In-progress'),
        ('COMPLETE', 'Complete'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, blank=True)
    task_body = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255, blank=True)
    priority = models.CharField(max_length=255,
                                choices=PRIORITY_CHOICES,
                                default='LOW')
    due_date = models.DateField(blank=True, null=True)
    files = models.FileField(blank=True)
    assigned_to = models.ForeignKey(User,
                                    null=True,
                                    on_delete=models.SET_NULL,
                                    related_name='assigned_to')
    # completed = models.BooleanField(default=False, blank=True, null=True)
    completed = models.CharField(max_length=255,
                                 choices=COMPLETION_STATUS,
                                 default='NO')
    pack = models.ForeignKey(Pack, on_delete=models.CASCADE, blank=True,
                             null=True)

    class Meta:
        ordering = ['due_date']

    def __str__(self):
        """
        Return information of the Task
        """
        return f"Task: #{self.id}"
