# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db.models import Count
from rest_framework import status, generics, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from django.contrib.auth.models import User

# Internal:
from .models import Profile
from .serializers import ProfileSerializer
from tick_it_drf_api.permissions import IsOwnerOrReadOnly
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class ProfileList(generics.ListAPIView):
    """
    List all profiles
    No Create view (post method), as profile creation
    handled by django signals
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
        tasks_count=Count(
            'owner__task',
            distinct=True),
        watching_count=Count(
            'owner__watch',
            distinct=True)
    ).order_by('-created_on')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    search_fields = [
        'owner__username',
    ]
    ordering_fields = [
        'tasks_count',
        'watching_count',
    ]


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]

    queryset = Profile.objects.annotate(
        tasks_count=Count(
            'owner__task',
            distinct=True),
        watching_count=Count(
            'owner__watch',
            distinct=True)
    ).order_by('-created_on')


class UserList(APIView):
    def get(self, request):
        users = User.objects.all().values()
        return Response(users)
