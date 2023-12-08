from rest_framework.routers import DefaultRouter
from .views import CustomUserModelViewSet


router = DefaultRouter()
router.register(r'clients', CustomUserModelViewSet, basename='client')

urlpatterns = router.urls