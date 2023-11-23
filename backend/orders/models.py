from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product

User = get_user_model()

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    total_sum = models.DecimalField(max_digits=9, decimal_places=2)
    zip_code = models.IntegerField()
    address = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=[('process', 'Process'), ('delivered', 'Delivered'), ('canceled', 'Canceled')])

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()