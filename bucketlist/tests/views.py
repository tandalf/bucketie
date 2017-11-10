import json

from django.test import TestCase
from django.db import models

from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework import status

from bucketie.tests.test_mixins import UtilsProviderTestMixin
from ..models import UserModel, BucketList, BucketListItem
from ..views import BucketListViewSet, BucketListItemViewSet

bucketlist_list_view = BucketListViewSet.as_view({'get': 'list'})
bucketlist_list_item_view = BucketListItemViewSet.as_view({'get': 'list'})

class TestBucketListViews(TestCase, UtilsProviderTestMixin):
    def setUp(self):
        super(TestBucketListViews, self).setUpUtilsProvider()

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
    
class TestBucketListItemViews(TestCase, UtilsProviderTestMixin):
    def setUp(self):
        super(TestBucketListItemViews, self).setUpUtilsProvider()

    def test_non_auth_users_get_permission_error_on_bucketlist_item_endpoint(self):
        #assert unauthenticated users will get an unauthories http response
        bucketlist = self.create_bucketlist(self.user1)
        request = self.factory.get('/bucketlist/{}/items/'.format(bucketlist.id))
        response = bucketlist_list_item_view(request)
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)

    def test_auth_users_get_error_on_listing_bucketlist_items_if_not_owner(self):
        bucketlist = self.create_bucketlist(self.admin1)
        #authenticate with a non-admin user
        self.client.force_authenticate(user=self.user2)
        response = self.client.get('/bucketlist/{}/items/'.format(bucketlist.id))
        print response.content
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)

    def test_auth_users_get_error_on_bucketlist_item_if_not_owner_or_assigned_user(self):
        """
        Check that non safe methods are not permitted is the acting user is not 
        the owner of the collection, or the assigned user in the bucketlist's item
        that is being accessed
        """
        pass