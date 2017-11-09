# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from bucketie.models import TimeStampedModel, DescribedModel

class BucketList(TimeStampedModel, DescribedModel):
    pass

class BucketListItem(TimeStampedModel, DescribedModel):
    pass
