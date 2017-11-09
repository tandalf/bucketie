from datetime import timedelta
from time import sleep

from django.test import TestCase
from django.db import models
from django.utils.timezone import now

from bucketie.models import TimeStampedModel, DescribedModel

class TimedModel(TimeStampedModel):
    is_modified = models.BooleanField(default=False)
    pass

class DetailedModel(DescribedModel):
    pass

class TestTimeStampedModels(TestCase):
    def test_created_at_field(self):
        create_start = now()
        timed = TimedModel()
        create_end = now()
        timed.save()
        self.assertGreater(timed.created_at, create_start)
        self.assertLess(timed.created_at, create_end)

    def test_modified_at_field(self):
        modified_start = now()
        timed = TimedModel()
        timed.save()
        modified_end = now()
        self.assertGreater(timed.modified_at, modified_start)
        self.assertLess(timed.modified_at, modified_end)

        #modify model and check modification time was updated
        sleep(0.1)
        timed.is_modified = True
        modified_start = now()
        timed.save()
        modified_end = now()
        self.assertGreater(timed.modified_at, modified_start)
        self.assertLess(timed.modified_at, modified_end)