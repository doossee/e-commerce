from django.contrib import admin
from .models import OrderItem, Order

class OrderItemInline(admin.StackedInline):
    model = OrderItem
    extra = 1

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id','order', 'product', 'quantity')
    list_display_links = ('order',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'user', 
        'total_sum', 
        'address', 
        'status',
        'delivery_type',
        'date_delivery',
        'created_at',
        'updated_at',
    )
    list_editable = ('status',)
    inlines = (OrderItemInline,)