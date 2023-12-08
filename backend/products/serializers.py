from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer
from rest_flex_fields import FlexFieldsModelSerializer
from .models import (
    Brand,
    Category,
    Color,
    Product,
    ProductUnit,
    Image,
    Rating
)

class BrandSerializer(serializers.ModelSerializer):

    """Brand Serializer"""

    class Meta:
        model = Brand
        fields = '__all__'


class AbstractCategorySerializer(FlexFieldsModelSerializer):

    """Abstract category serializer"""

    class Meta:
        model = Category
        fields = (
            'id',
            'lft',
            'rght',
            'tree_id',
            'level',
            'name_en',
            'name_ru',
            'name_uz',
            'parent',
        )
        depth = 3
        

class CategorySerializer(AbstractCategorySerializer):

    """Category serializer"""
    
    children = serializers.SerializerMethodField()

    def get_children(self, instance):
        
        children = instance.get_children()
        serializer = CategorySerializer(children, many=True)
        return serializer.data
    
    class Meta:
        model = Category
        depth = 5
        fields = (
            'id',
            'lft',
            'rght',
            'tree_id',
            'level',
            'name_en',
            'name_ru',
            'name_uz',
            'children'
        )
        

class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):

    """Image serializer"""

    image = VersatileImageFieldSerializer(sizes='product_headshot')
    class Meta:
        model = Image
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):

    """Rating serializer"""

    class Meta:
        model = Rating
        fields = '__all__'


class ProductUnitSerializer(serializers.ModelSerializer):

    """Product unit serializer"""
    product_title = serializers.CharField(source='product.title')
    image = VersatileImageFieldSerializer(sizes='product_headshot')

    class Meta:
        model = ProductUnit
        fields = '__all__'


class ProductSerializer(FlexFieldsModelSerializer):
    
    """Product Serializer"""

    # category = AbstractCategorySerializer()
    # brand = BrandSerializer()
    # ratings = RatingSerializer(many=True)
    # images = ImageSerializer(many=True)
    rating = serializers.DecimalField(max_digits=3, decimal_places=2)
    class Meta:
        model = Product
        # exclude = (
        #     'is_published',
        #     'i18n',
        #     'description',
        #     'usage',
        #     'description_i18n',
        #     'usage_i18n',
        # )
        fields = (
            'id',
            'title',
            'description_en',
            'description_ru',
            'description_uz',
            'usage_en',
            'usage_ru',
            'usage_uz',
            'created_at',
            'updated_at',
            'category',
            'brand',
            'colors',
            'price',
            'discount',
            'rating',
            'is_gift',
            'images',
            'ratings',
            'units'
        )
        expandable_fields = {
            'category': AbstractCategorySerializer,
            'brand': BrandSerializer,
            'colors': (ColorSerializer, {'many': True}),
            'units': (ProductUnitSerializer, {'many': True}),
            'ratings': (RatingSerializer, {'many': True}),
            'images': (ImageSerializer, {'many': True}),
        }