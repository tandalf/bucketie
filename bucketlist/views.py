# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Q

from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import UserModel, BucketList, BucketListItem
from .serializers import (
    BucketListSerializer, BucketListItemSerializer, RetrieveUserSerializer 
)
from .permissions import (
    OnlyBucketListOwnerCanListPermission, OwnerOrAssignedUserPermission, OwnerOnlyPermission
)

class UserView(generics.RetrieveAPIView):
    queryset = UserModel.objects.all()
    serializer_class = RetrieveUserSerializer

class BucketListViewSet(viewsets.ModelViewSet):
    """
    View set created with the responsibility of getting,  listing, retrieving or 
    deleting BucketList views
    """ 
    serializer_class = BucketListSerializer
    permission_classes = (IsAuthenticated, IsAdminUser, OwnerOnlyPermission)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        """
        Filters the querset to allow only the owners of the BucketList to take 
        action on them
        """
        user = self.request.user
        return BucketList.objects.filter(owner=user)


class BucketListItemViewSet(viewsets.ModelViewSet):
    """
    ViewSet assigned the responsibility of getting,  listing, retrieving or 
    deleting BucketList views
    """
    serializer_class = BucketListItemSerializer
    permission_classes = (IsAuthenticated, OnlyBucketListOwnerCanListPermission)

    def get_queryset(self):
        """
        Filter the queryset to allow only the assigned user of the BucketListItem
        and the owner of the containing BucketList to access the items.
        """
        user = self.request.user
        return BucketListItem.objects.filter(Q(assigned_user=user.pk) | 
            Q(bucketlist__owner=user.pk))