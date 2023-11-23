from .models import (
    Order,
    OrderItem
)
from .serializers import (
    OrderItemSerializer,
    OrderSerializer
)
from rest_framework import viewsets

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer