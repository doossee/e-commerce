from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import (
    Brand,
    Category,
    ProductColor,
    Product,
    Rating,
    Review,
    Image,
)

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    model = Brand
    list_display = ('name',)

@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    list_display = ('tree_actions', 'indented_title')
    list_filter = ('parent',)

    def indented_title(self, instance):
        return mark_safe(
            '<div style="text-indent:{}px">{}</div>'.format(
                instance.level * 20,  # Adjust the multiplier for the desired indentation
                escape(instance.name)
            )
        )

    indented_title.short_description = 'Indented Title'

# class BrandAdmin(admin.ModelAdmin):
#     model = Brand
#     fields = '__all__'

# class BrandAdmin(admin.ModelAdmin):
#     model = Brand
#     fields = '__all__'

# class BrandAdmin(admin.ModelAdmin):
#     model = Brand
#     fields = '__all__'

# class BrandAdmin(admin.ModelAdmin):
#     model = Brand
#     fields = '__all__'

