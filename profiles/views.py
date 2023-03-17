# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db.models import Count
from rest_framework import status, generics, filters
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

# Internal:
from .models import Profile
from .serializers import ProfileSerializer
from tick_it_drf_api.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
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
    # def get_object(self, pk):
    #     try:
    #         profile = Profile.objects.get(pk=pk)
    #         self.check_object_permissions(self.request, profile)
    #         return profile
    #     except Profile.DoesNotExist:
    #         raise Http404

    # def get(self, request, pk):
    #     profile = self.get_object(pk)
    #     serializer = ProfileSerializer(profile,
    #                                    context={'request': request})
    #     return Response(serializer.data)

    # def put(self, request, pk):
    #     profile = self.get_object(pk)
    #     serializer = ProfileSerializer(profile,
    #                                    data=request.data,
    #                                    context={'request': request})
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
