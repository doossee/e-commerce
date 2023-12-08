from rest_framework import permissions

class IsOwnerOrReadonly(permissions.BasePermission):

    def has_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS
        )
    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in permissions.SAFE_METHODS or
            request.user == obj.user
        )