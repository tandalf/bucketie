# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets, generics

from .models import UserModel, BucketList
from .serializers import BucketListSerializer, RetrieveUserSerializer

class UserView(generics.RetrieveAPIView):
    queryset = UserModel.objects.all()
    serializer_class = RetrieveUserSerializer

class BucketListViewSet(viewsets.ModelViewSet):
    """
    View set created with the responsibility of listing, retrieving or deleting
    BucketList views
    """
    queryset = BucketList.objects.all()
    serializer_class = BucketListSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)