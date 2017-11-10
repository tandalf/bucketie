"""
This module contains reuseable code that can be used by various test code
throughout this application
"""
from rest_framework.authtoken.models import Token
from rest_framework.test import APIRequestFactory, APIClient

from bucketlist.models import UserModel, BucketList

class UtilsProviderTestMixin(object):
    def setUpUtilsProvider(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.admin1 = UserModel.objects.create_user(username='tim', 
            email='tim@live.com', password='top_secret')
        self.user1 = UserModel.objects.create_user(username='timo', 
            email='timo@live.com', password='top_secret')
        self.user2 = UserModel.objects.create_user(username='timu', 
            email='timu@live.com', password='top_secret')

    def set_client_credentials(self, user):
        #token = Token.objects.get(user__username=user.username)
        #self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        pass

    def create_bucketlist(self, user, name="My Bucketlist", description="B"):
        bucketlist = BucketList(owner=user, name=name, description=description)
        bucketlist.save()
        return bucketlist