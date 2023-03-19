# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models
from django.contrib.auth.models import User

# Internal:
# from tasks.models import Task
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Pack(models.Model):
    """
    A class for the pack model
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, blank=False)
    pack_description = models.TextField(blank=True)
    members = models.ManyToManyField(User, related_name='members')
    updated_on = models.DateTimeField(auto_now=True)
    tasks = models.ForeignKey("tasks.Task", on_delete=models.CASCADE,
                              related_name="task")

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        """
        Return information of the Pack
        """
        return f"{self.title}"
