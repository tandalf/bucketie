from datetime import timedelta

from django.test import TestCase
from django.utils.timezone import now

from bucketie.models import TimeStampedModel, DescribedModel

class TimedModel(TimeStampedModel):
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
        create_start = now()
        timed = TimedModel()
        create_end = now()
        timed.save()

        self.assertGreater(timed.modified_at, create_start)
        self.assertLess(timed.modified_at, create_end)