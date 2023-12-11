from rest_framework import serializers

from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    
    """Order item serializer"""

    # product = ProductUnitSerializer()

    class Meta:
        model = OrderItem
        fields = (
            'order',
            'product',
            'quantity'
        )
        extra_kwargs = {
            'order': {'required': False}
        }

    def validate(self, attrs):
        if attrs['quantity'] > attrs['product'].balance:
            raise serializers.ValidationError("There is no so much products")
        return attrs


class OrderSerializer(serializers.ModelSerializer):
    
    """Order serializer"""

    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = [
            'id',
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

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        print(order)

        for item_data in items_data:
            product_data = item_data.pop('product')
            order_item = OrderItem.objects.create(order=order, product=product_data, **item_data)

        return order
    