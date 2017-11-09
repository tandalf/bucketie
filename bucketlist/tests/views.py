import json

from django.test import TestCase
from django.db import models

from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework import status

from ..models import UserModel, BucketList, BucketListItem
from ..views import BucketListViewSet

bucketlist_list_view = BucketListViewSet.as_view({'get': 'list'})

class TestBucketListViews(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.admin1 = UserModel.objects.create_user(username='tim', 
            email='tim@live.com', password='top_secret')
        self.user1 = UserModel.objects.create_user(username='timo', 
            email='timo@live.com', password='top_secret')
        self.user2 = UserModel.objects.create_user(username='timu', 
            email='timu@live.com', password='top_secret')

    def create_bucketlist(self, user, name="My Bucketlist", description="B"):
        bucketlist = BucketList(owner=user, name=name, description=description)
        bucketlist.save()
        return bucketlist

    def test_non_auth_users_get_permission_error_on_bucketlist_endpoint(self):
        #assert unauthenticated users will get an unauthories http response
        request = self.factory.get('/bucketlist/')
        response = bucketlist_list_view(request)
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)

    def test_auth_users_get_forbidden_error_on_bucketlist_endpoint_if_not_admin(self):
        #assert that authenticated but non-admin users cant access the endpoint
        request = self.factory.get('/bucketlist/')
        bucketlist = self.create_bucketlist(self.user1)
        force_authenticate(request, user=self.user1)
        response = bucketlist_list_view(request)
        response.render()
        data = json.loads(response.content)

        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)
    