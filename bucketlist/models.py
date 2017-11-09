# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

from bucketie.models import TimeStampedModel, DescribedModel

class BucketList(TimeStampedModel, DescribedModel):
    """
    BucketList model which will act as a container for BucketList items
    """
    pass

class BucketListItem(TimeStampedModel, DescribedModel):
    """
    Model which represents the items that are stored in a BucketList
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    done = models.BooleanField(default=False)

    def mark_done(self):
        """Mark this BucketList Item as done"""
        self.done = True
        self.save()
