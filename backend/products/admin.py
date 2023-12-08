from django.contrib import admin
from django.db import models
from django import forms
from mptt.admin import DraggableMPTTAdmin
from django.utils.translation import gettext_lazy as _
from django.utils.html import mark_safe, escape

from .models import (
    Brand,
    Category,
    Color,
    Product,
    ProductUnit,
    Rating,
    Image,
)


class BrandInline(admin.StackedInline):
    model = Brand
    min_num = 1 

class CategoryInline(admin.StackedInline):
    model = Category

class ColorInline(admin.StackedInline):
    model = Color

class ProductInline(admin.StackedInline):
    model = Product

class ProductUnitInline(admin.StackedInline):
    model = ProductUnit
    extra = 1

    def get_queryset(self, request):
        qs = ProductUnit.objects.all()\
                .select_related(
                    'product',
                    'color'
                )\
            
class RatingInline(admin.StackedInline):
    model = Rating
    extra = 1

class ImageInline(admin.StackedInline):
    model = Image
    extra = 1
    def get_queryset(self, request):
        qs = Image.objects.all()\
                .select_related('product')
        return qs


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    model = Brand
    list_display = ('name', 'description')
    formfield_overrides = {
        models.CharField: {'widget': forms.widgets.TextInput(attrs={})},
        models.TextField: {'widget': forms.widgets.Textarea(attrs={"cols": "200", "rows": "2"})},
    }
    fieldsets = (
        (_('NAME'),{
            'fields': ('name',),
            'classes': ('wide',),
        }),
        (_('DESCRIPTION'),{
            'fields': ('description_en', 'description_ru', 'description_uz'),
            'classes': ('wide',),
        }),
    )


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title', 'name', 'parent')
    list_filter = ('parent',)
    fieldsets = (
        (_('NAME'),{
            'fields': ('name_en', 'name_ru', 'name_uz'),
            'classes': ('wide'),
        }),
        (_('PARENT'),{
            'fields': ('parent',),
            'classes': ('wide',),
        }),
    )

    def indented_title(self, instance):
        return mark_safe(
            '<div style="text-indent:{}px">{}</div>'.format(
                instance.level * 20,  # Adjust the multiplier for the desired indentation
                escape(instance.name)
            )
        )

    indented_title.short_description = 'Indented Title'


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'hex'
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'usage',
        'category',
        'brand',
        'display_colors',
        'price',
        'discount',
        'display_balance_sum',
        'display_rating',
        'is_published',
        'is_gift',
    )
    list_editable = (
        'is_published',
        'is_gift',
    )
    list_select_related = (
        'brand',
        'category'
    )
    formfield_overrides = {
        models.CharField: {'widget': forms.widgets.TextInput(attrs={})},
        models.TextField: {'widget': forms.widgets.Textarea(attrs={"cols": "200", "rows": "2"})},
    }
    fieldsets = (
        (_('TITLE'),{
            'fields': ('title',),
            'classes': ('wide'),
        }),
        (_('DESCRIPTION'),{
            'fields': ('description_en', 'description_ru', 'description_uz'),
            'classes': ('wide',),
        }),
        (_('USAGE'),{
            'fields': ('usage_en', 'usage_ru', 'usage_uz'),
            'classes': ('wide',),
        }),
        (_('CATEGORY AND BRAND'),{
            'fields': ('category','brand'),
            'classes': ('wide',),
        }),
        (_('PRICE AND DISCOUNT'),{
            'fields': ('price', 'discount'),
            'classes': ('wide',),
        }),
        (_('PUBLISH AND GIFT'),{
            'fields': ('is_published', 'is_gift'),
            'classes': ('wide',),
        }),
    )
    inlines = (ImageInline, ProductUnitInline)

    def get_queryset(self, request):
        qs = Product.objects.all()\
                .select_related(
                    'brand',
                    'category',
                )\
                .prefetch_related(
                    'colors',
                    'ratings',
                    'images',
                    'units',
                )\
                .annotate(balance_sum=models.Sum('units__balance'))\
                .annotate(rating=models.Avg('ratings__rate'))
        return qs

    def display_balance_sum(self, instance):
        return instance.balance_sum
    
    def display_colors(self, instance):
        return ", ".join([color.name for color in instance.colors.all()])

    def display_rating(self, instance):
        return instance.rating
    
    display_colors.short_description = 'Colors'
    display_balance_sum.short_description = 'Balance'
    display_rating.short_description = 'Rating'


# @admin.register(ProductUnit)
# class ProductUnit(admin.ModelAdmin):
#     list_display = ('product', 'color', 'balance')
#     # inlines = (ProductInline, ColorInline)
    

# @admin.register(Rating)
# class RatingAdmin(admin.ModelAdmin):
#     model = Rating
#     list_display = ('id', 'user', 'product', 'rate', 'review')
#     list_display_links = ('user', )
#     list_editable = ('rate', )


# @admin.register(Image)
# class ImageAdmin(admin.ModelAdmin):
#     model = Image
#     list_display = ('id', 'product',)