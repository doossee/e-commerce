from rest_framework.viewsets import GenericViewSet 
from rest_framework.generics import mixins 
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth import get_user_model
from .serializers import CustomUserSerializer

class IsOwnerOrAuthenticatedReadOnly(IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        return bool(
            request.user == obj.user
        )

User = get_user_model()

class CustomUserModelViewSet(
                mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.ListModelMixin, 
                GenericViewSet):
    
    serializer_class = CustomUserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    
    def get_queryset(self):
        user_id = self.request.user.id
        qs = User.objects.all().filter(id=user_id)
        return qs

