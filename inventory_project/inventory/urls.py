from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, SupplierViewSet, ProductViewSet, CustomerViewSet, OrderViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('suppliers', SupplierViewSet)
router.register('products', ProductViewSet)
router.register('customers', CustomerViewSet)
router.register('orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
