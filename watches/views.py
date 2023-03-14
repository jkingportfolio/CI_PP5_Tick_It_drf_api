# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from rest_framework import generics, permissions
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Internal:
from .models import Watch
from .serializers import WatchSerializer
from tick_it_drf_api.permissions import IsOwnerOrReadOnly
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class WatchList(generics.ListCreateAPIView):
    """
    A class for WatchList
    """
    serializer_class = WatchSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
        ]
    queryset = Watch.objects.all()

    def perform_create(self, serializer):
        # owner is the user making the request
        serializer.save(owner=self.request.user)


class WatchDetail(generics.RetrieveDestroyAPIView):
    """
    A class for WatchDetail
    User to be able to retrieve and delete their watch
    of a task
    """
    serializer_class = WatchSerializer
    permission_classes = [
        IsOwnerOrReadOnly
        ]
    queryset = Watch.objects.all()
