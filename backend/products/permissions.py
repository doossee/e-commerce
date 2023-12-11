from rest_framework import permissions

class IsOwnerOrReadonly(permissions.BasePermission):

    """Owner can change the object and all can view list of objects"""

    def has_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS
        )
    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in permissions.SAFE_METHODS or
            request.user == obj.user
        )
