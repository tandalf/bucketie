from rest_framework import serializers

from .models import UserModel, BucketList, BucketListItem

class RetrieveUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'url', 'username', 'first_name', 'last_name')
        read_only_fields = ('id', 'url', 'username', 'first_name', 'last_name')

class BucketListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BucketList
        fields = ('url', 'owner', 'name', 'description', 'created_at', 'modified_at')
        read_only_fields = ('url', 'owner', 'created_at', 'modified_at')
        

class BucketListItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BucketListItem
        fields = ('url', 'owner', 'name', 'description', 'done', 'created_at', 
            'modified_at')
        read_only_fields = ('url', 'owner', 'created_at', 'modified_at')