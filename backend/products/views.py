from rest_framework import viewsets
from django.db.models import Avg
from rest_flex_fields.views import FlexFieldsMixin
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_flex_fields import is_expanded

from .permissions import IsOwnerOrReadonly
from .pagination import CustomPagination
from .filters import ProductFilter
from .models import (
    Brand,
    Category,
    Product,
    # ProductUnit,
    Rating,
    # Image,
)
from .serializers import (
    BrandSerializer,
    AbstractCategorySerializer,
    CategorySerializer,
    RatingSerializer,
    ProductSerializer,
)

class BrandViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class CategoryViewSet(FlexFieldsMixin,viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all().select_related('parent').filter(parent=None)
    serializer_class = CategorySerializer
    permission_classes = [IsOwnerOrReadonly,]


# class ProductColorViewset(viewsets.ReadOnlyModelViewSet):
#     queryset = Color.objects.all()
#     serializer_class = 
#     permission_classes = [IsAdminOrReadOnly,]


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,]


class ProductViewSet(FlexFieldsMixin, viewsets.ReadOnlyModelViewSet):
    
    """Products relation"""

    # permission_classes = [IsOwnerOrReadonly,]
    serializer_class = ProductSerializer
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = ProductFilter
    search_fields = ['title',]
    ordering_fields = ['created_at', 'rating']
    permit_list_expands = [
        'category', 
        'brand', 
        'colors', 
        'ratings',  
        'images',
        'units'
    ]
    
    def get_queryset(self):

        queryset = Product.objects.all()\
                .prefetch_related('colors')\
                    .annotate(rating=Avg('ratings__rate'))

        if is_expanded(self.request, 'category'):
            queryset = queryset.select_related('category')

        # if is_expanded(self.request, 'brand'):
        #     queryset = queryset.select_related('brand')

        if is_expanded(self.request, 'units'):
            queryset = queryset.prefetch_related('units')

        if is_expanded(self.request, 'ratings'):
            queryset = queryset.prefetch_related('ratings')

        if is_expanded(self.request, 'images'):
            queryset = queryset.prefetch_related('images')
        
        return queryset
