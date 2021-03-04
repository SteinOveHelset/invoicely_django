from rest_framework import serializers

from .models import Team

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        read_only_fields = (
            "created_by",
        ),
        fields = (
            "id",
            "name",
            "org_number",
            "first_invoice_number",
            "bankaccount"
        )