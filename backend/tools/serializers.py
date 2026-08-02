from rest_framework import serializers
from .models import Tool


class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = ["id", "title", "slug", "category", "description", "url", "order", "created_at"]
