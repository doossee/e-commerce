from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrAuthenticated(BasePermission):

    """
    Only owners or authenticated users 
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated) 
    
    def has_object_permission(self, request, view, obj):
        return bool(request.user == obj.user)
    