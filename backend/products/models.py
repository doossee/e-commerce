from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth import get_user_model
from versatileimagefield.fields import VersatileImageField, PPOIField

User = get_user_model()

class Brand(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    

class Category(MPTTModel):
    name = models.CharField(max_length=100)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    
class ProductColor(models.Model):
    name = models.CharField(max_length=100)
    hex_code = models.CharField(max_length=7)


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    usage = models.TextField()
    category = models.ForeignKey(to=Category, null=True, on_delete=models.SET_NULL)
    brand = models.ForeignKey(to=Brand, null=True, on_delete=models.SET_NULL)
    color = models.ManyToManyField(to=ProductColor)
    
    price = models.DecimalField(max_digits=9, decimal_places=2)
    discount = models.PositiveSmallIntegerField()
    balance = models.PositiveBigIntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=2)

    is_published = models.BooleanField(default=False)
    is_gift = models.BooleanField(default=False)


class Rating(models.Model):
    user = models.ForeignKey(to=User, related_query_name='ratings', on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, related_name='ratings', on_delete=models.CASCADE)
    rate = models.PositiveSmallIntegerField()


class Review(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, related_name='reviews', on_delete=models.CASCADE)


class Image(models.Model):
    name = models.CharField(max_length=255)
    image = VersatileImageField(
        'Image',
        upload_to='images/',
        ppoi_field='image_ppoi'
    )
    image_ppoi = PPOIField()

    def __str__(self):
        return self.name


