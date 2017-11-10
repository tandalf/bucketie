from rest_framework import permissions

class OwnerOnlyPermission(permissions.BasePermission):
    message = 'Not Allowed'

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

class OwnerAndAssignedUserPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.assgined_user == request.user or \
            obj.bucketlist.owner == request.user