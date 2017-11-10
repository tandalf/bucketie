"""
This module contains reuseable code that can be used by various test code
throughout this application
"""
from rest_framework.test import APIRequestFactory

from bucketlist.models import UserModel

class UtilsProviderTestMixin(object):
    def setUpUtilsProvider(self):
        self.factory = APIRequestFactory()
        self.admin1 = UserModel.objects.create_user(username='tim', 
            email='tim@live.com', password='top_secret')
        self.user1 = UserModel.objects.create_user(username='timo', 
            email='timo@live.com', password='top_secret')
        self.user2 = UserModel.objects.create_user(username='timu', 
            email='timu@live.com', password='top_secret')