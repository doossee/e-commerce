from .models import (
    Brand,
    Category,
    ProductColor,
    Product,
    Rating,
    Review,
    Image,
)
from .serializers import (
    BrandSerializer,
    CategorySerializer,
    ProductColorSerializer,
    RatingSerializer,
    ReviewSerializer,
    ImageSerializer,
    ProductSerializer
)
from rest_framework import viewsets

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductColorViewset(viewsets.ModelViewSet):
    queryset = ProductColor.objects.all()
    serializer_class = ProductColorSerializer

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.object.all()
    serializer_class = ReviewSerializer

class ImageViewset(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class Product(viewsets.ModelViewSet):
    queryset = Product.object.all()
    serializer_class = ProductSerializer