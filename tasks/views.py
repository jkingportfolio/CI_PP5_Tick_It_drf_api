# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Internal:
from .models import Task
from .serializers import TaskSerializer
from tick_it_drf_api.permissions import IsOwnerOrReadOnly
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TaskList(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Task.objects.annotate(
        comments_count=Count(
            'comments',
            distinct=True
        ),
    ).order_by('-created_on')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    ordering_fields = [
        'comments_number',
    ]
    search_fields = [
        'owner__username',
        'title',
        'completed',
        'priority',
    ]
    filterset_fields = [
        'watches__owner__profile',
        'owner__profile',
        'completed',
        'priority',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = TaskSerializer

    queryset = Task.objects.annotate(
        comments_count=Count(
            'comments',
            distinct=True
        ),
    ).order_by('-created_on')
