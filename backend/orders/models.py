from django.db import models
from django.contrib.auth import get_user_model
from django.forms import ValidationError
from products.models import ProductUnit

User = get_user_model()


class AbstractOrder(models.Model):
    
    """Abstract Order Model"""

    user = models.ForeignKey(to=User, related_name='orders', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Order(AbstractOrder):

    """Order Model"""

    total_sum = models.PositiveIntegerField(default=0)
    address = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=[('process', 'Process'), ('delivered', 'Delivered'), ('canceled', 'Canceled')])
    delivery_type = models.CharField(max_length=50)
    date_delivery = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f"{self.user}-{self.status}"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.status == 'cancelled':
            for order_item in self.items.all():
                product = order_item.product
                product.balance += order_item.quantity
                product.save()


class OrderItem(models.Model):

    """Order Item Model"""

    order = models.ForeignKey(to=Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(to=ProductUnit, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = 'Order item'
        verbose_name_plural = 'Order items'

    def clean(self):
        if self.quantity > self.product.balance:
            raise ValidationError('Quantity cannot be greater than the product balance.')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

        self.product.balance -= self.quantity
        self.product.save()
    
    def __str__(self):
        return f"{self.product}-{self.quantity}"