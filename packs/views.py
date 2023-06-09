# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Internal:
from .models import Pack
from .serializers import PackSerializer, PackDetailSerializer
from tick_it_drf_api.permissions import IsOwnerOrReadOnly
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class PackList(generics.ListCreateAPIView):
    """
    A class for PackList
    """
    serializer_class = PackSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
        ]
    queryset = Pack.objects.all()
    filterset_fields = [
        'pack__tasks',
    ]
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    search_fields = [
        'owner__username',
        'title',
    ]
    filterset_fields = [
        'owner__profile',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PackDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    A class to retrieve a pack list
    an update / delete it by id.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PackDetailSerializer
    queryset = Pack.objects.all()
