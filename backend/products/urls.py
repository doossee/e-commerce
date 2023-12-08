from rest_framework.routers import DefaultRouter
from .views import (
   BrandViewSet,
   CategoryViewSet,
   # ProductColorViewset,
   RatingViewSet,
   # ImageViewSet,
   ProductViewSet,
)

router = DefaultRouter()
router.register(r'brands', BrandViewSet, basename='brand')
router.register(r'categories', CategoryViewSet, basename='category')
# router.register(r'colors', ProductColorViewset, basename='color')
router.register(r'ratings', RatingViewSet, basename='rating')
# router.register(r'images', ImageViewSet, basename='image')
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = router.urls