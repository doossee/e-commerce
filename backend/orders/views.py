from rest_framework import viewsets
from rest_flex_fields.views import FlexFieldsMixin
from django_filters import rest_framework as filters
from .permissions import IsOwnerOrAuthenticated 
from .models import Order
from .serializers import OrderSerializer


class OrderViewSet(FlexFieldsMixin, viewsets.ModelViewSet):

    """Order view"""
    pagination_class = None
    serializer_class = OrderSerializer
    permission_classes = [IsOwnerOrAuthenticated,]

    def get_queryset(self):
        user_id = self.request.user.id 
        print(user_id)
        qs = Order.objects\
            .filter(user=user_id)\
            .prefetch_related('items')
        print(self.request.user)
        return qs