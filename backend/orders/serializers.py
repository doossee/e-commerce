from rest_framework import serializers
from .models import Order, OrderItem
from rest_flex_fields import FlexFieldsModelSerializer
from products.serializers import ProductUnitSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    
    """Order item serializer"""

    product = ProductUnitSerializer()

    class Meta:
        model = OrderItem
        fields = '__all__'
        expandable_fields = {
            'product': ProductUnitSerializer,
        }


class OrderSerializer(FlexFieldsModelSerializer):
    
    """Order serializer"""

    class Meta:
        model = Order
        fields = [
            'user',
            'created_at',
            'updated_at',
            'total_sum',
            'address',
            'status',
            'delivery_type',
            'date_delivery',
            'items',
        ]
        expandable_fields = {
            'items': (OrderItemSerializer, {'many': True}),
        }
