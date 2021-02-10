from rest_framework import serializers

from .models import Invoice, Item

class InvoiceSerializer(serializers.ModelSerializer):   
    client = serializers.StringRelatedField()

    class Meta:
        model = Invoice
        read_only_fields = (
            "team",
            "invoice_number",
            "created_at",
            "created_by",
            "modified_at",
            "modified_by",
        ),
        fields = (
            "id",
            "invoice_number",
            "client",
            "client_name",
            "client_email",
            "client_org_number",
            "client_address1",
            "client_address2",
            "client_zipcode",
            "client_place",
            "client_country",
            "client_contact_person",
            "client_contact_reference",
            "sender_reference",
            "invoice_type",
            "due_days",
            "is_sent",
            "is_paid",
            "gross_amount",
            "vat_amount",
            "net_amount",
            "discount_amount",
        )

class ItemSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Item
        read_only_fields = (
            "invoice",
        )
        fields = (
            "id",
            "title",
            "quantity",
            "unit_price",
            "net_amount",
            "vat_rate",
            "discount"
        )