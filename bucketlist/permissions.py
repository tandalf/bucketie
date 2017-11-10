from rest_framework import permissions

from .models import BucketList

class OwnerOnlyPermission(permissions.BasePermission):
    message = 'Not Allowed'

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

class OnlyParentResourceOwnerCanList(permissions.BasePermission):
    """
    Base Permission class that permits only the owner of a parent resource in a nested
    view to list the children of that nested view E.g /containter/1/items
    will be permitted only if the current user is the owner of the container 1.
    That is, the user will only be allowed to list the items in the container
    if he is the owner of the container. 
    Note that this does not prevent the user from acccessing a SINGLE item in the
    container E.g /container/1/items/1 is allowed even if the user is not the owner
    of the container

    This Permission class is designed to be used in drf_extension nested viewsets.
    """
    def has_permission(self, request, view):
        if request.method == 'GET':
            parent_resource_class = self.get_parent_class()
            parent_resource_id = self.get_parent_id(request)
            #print '{} - {}'.format(parent_resource_class, parent_resource_id)
            return parent_resource_class.objects.filter(pk=parent_resource_id, 
                owner=request.user.id).exists()

    def get_parent_class(self):
        return self.__class__.Meta.parent_model

    def get_parent_id(self, request):
        parent_resource_lookup = self.__class__.Meta.parent_lookup
        return request.resolver_match.kwargs.get('parent_lookup_{}'.format(
            parent_resource_lookup))

class OnlyBucketListOwnerCanListPermission(OnlyParentResourceOwnerCanList):
    class Meta:
        parent_model = BucketList
        parent_lookup = 'bucketlist'

class OwnerOrAssignedUserPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.assgined_user == request.user or \
            obj.bucketlist.owner == request.user