# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

from bucketie.models import TimeStampedModel, DescribedModel

def default_user():
    user_id = -1
    try:
        user_id = get_user_model().objects.get(username='superuser').id
    except:
        pass

    return user_id

class BucketList(TimeStampedModel, DescribedModel):
    """
    BucketList model which will act as a container for BucketList items
    """
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        default=default_user)

    def add_item(self, item, save=False, *args, **kwargs):
        """
        Convinience method for adding items to a BucketList
        """
        self.items.add(item)
        if save:
            self.save()

class BucketListItem(TimeStampedModel, DescribedModel):
    """
    Model which represents the items that are stored in a BucketList
    """
    bucketlist = models.ForeignKey(BucketList, on_delete=models.CASCADE,
        related_name='items', default=-1)
    assigned_user = models.ForeignKey(settings.AUTH_USER_MODEL, 
        default=default_user)
    done = models.BooleanField(default=False)

    def mark_done(self):
        """Mark this BucketList Item as done"""
        self.done = True
        self.save()
