from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import InvoiceViewSet, ItemViewSet

router = DefaultRouter()
router.register("invoices", InvoiceViewSet, basename="invoices")
router.register("items", ItemViewSet, basename="items")

urlpatterns = [
    path('', include(router.urls)),
]