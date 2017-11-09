# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import UserModel, BucketList
from .serializers import BucketListSerializer, RetrieveUserSerializer
from .permissions import OwnerOnlyPermission

class UserView(generics.RetrieveAPIView):
    queryset = UserModel.objects.all()
    serializer_class = RetrieveUserSerializer

class BucketListViewSet(viewsets.ModelViewSet):
    """
    View set created with the responsibility of listing, retrieving or deleting
    BucketList views
    """
    serializer_class = BucketListSerializer
    permission_classes = (IsAuthenticated, IsAdminUser, OwnerOnlyPermission)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        user = self.request.user
        return BucketList.objects.filter(owner=user)