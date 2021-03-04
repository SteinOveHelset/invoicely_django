from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import InvoiceViewSet, generate_pdf

router = DefaultRouter()
router.register("invoices", InvoiceViewSet, basename="invoices")

urlpatterns = [
    path('', include(router.urls)),
    path('invoices/<int:invoice_id>/generate_pdf/', generate_pdf, name='generate_pdf'),
]