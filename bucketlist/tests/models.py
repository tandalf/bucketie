from datetime import datetime

from django.test import TestCase
from django.db import models
from django.contrib.auth import get_user_model

from ..models import BucketList, BucketListItem

UserModel = get_user_model()
def create_admin_with_bucketlist(username="tim", email='tim@live.com', 
    date_of_birth=datetime.now(), password='32fin034f'):

    admin = UserModel.objects.create_superuser(username=username, 
        email=email, password=password)
    blist = BucketList(owner=admin)
    blist.save()
    return admin, blist

class TestBucketListItems(TestCase):
    def test_add_items(self):
        admin, bucket_list = create_admin_with_bucketlist()
        item = BucketListItem(assigned_user=admin)
        item.save()

        #confirm items can be added to bucketlist
        bucket_list.add_item(item)
        bucket_list.refresh_from_db()
        self.assertEqual(bucket_list.items.all()[0], item)