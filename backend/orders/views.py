from rest_framework import viewsets
from rest_flex_fields.views import FlexFieldsMixin
from django_filters import rest_framework as filters
from .permissions import IsOwnerOrReadOnly 
from products.pagination import CustomPagination
from .models import Order
from .serializers import OrderSerializer


class OrderViewSet(FlexFieldsMixin, viewsets.ModelViewSet):
    queryset = Order.objects.all()\
        .prefetch_related('items')
    serializer_class = OrderSerializer
    permission_classes = [IsOwnerOrReadOnly,]
    # pagination_class = CustomPagination
    permit_list_expands = [
        'items',
    ]
