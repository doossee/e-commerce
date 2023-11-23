from rest_framework import serializers
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'

    # def create(self, validated_data):
    #     items_data = validated_data.pop('items')
    #     order = Order.objects.create(**validated_data)

    #     for item_data in items_data:
    #         OrderItem.objects.create(order=order, **item_data)

    #     return order

    # def update(self, instance, validated_data):
    #     items_data = validated_data.pop('items')
    #     instance.user = validated_data.get('user', instance.user)
    #     instance.date = validated_data.get('date', instance.date)
    #     instance.total_sum = validated_data.get('total_sum', instance.total_sum)
    #     instance.zip_code = validated_data.get('zip_code', instance.zip_code)
    #     instance.address = validated_data.get('address', instance.address)
    #     instance.status = validated_data.get('status', instance.status)
    #     instance.save()

    #     # Update or create each order item
    #     for item_data in items_data:
    #         order_item, created = OrderItem.objects.update_or_create(
    #             order=instance,
    #             product=item_data['product'],
    #             defaults={'quantity': item_data['quantity']}
    #         )

    #     return instance