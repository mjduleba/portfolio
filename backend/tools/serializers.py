from rest_framework import serializers
from .models import Tool, SkillAgentEntry


class SkillAgentEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillAgentEntry
        fields = ["name", "kind", "description", "tags", "video_url", "image_url"]


class ToolSerializer(serializers.ModelSerializer):
    skill_agent_entries = SkillAgentEntrySerializer(many=True, read_only=True)

    class Meta:
        model = Tool
        fields = [
            "id", "title", "slug", "category", "description", "url", "order",
            "created_at", "skill_agent_entries",
        ]
