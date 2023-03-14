# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models
from django.contrib.auth.models import User
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Internal:
from tasks.models import Task
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Watch(models.Model):
    """
    A class for the watch model
    Related to 'owner' and 'tasks'
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name='watches'
        )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        # 'unique_together' prevents user from watching the same task twice
        # https://docs.djangoproject.com/en/4.1/ref/models/options/#unique-together
        unique_together = ['owner', 'task']
        ordering = ['created_on']

    def __str__(self):
        return f'{self.owner} is watching task #{self.task.id}.'
