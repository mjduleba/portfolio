from rest_framework import serializers
from .models import Tool, SkillAgentEntry, GuidePattern, GuideExampleProblem


class SkillAgentEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillAgentEntry
        fields = ["name", "kind", "description", "tags", "video_url", "image_url"]


class GuideExampleProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuideExampleProblem
        fields = ["title", "description", "url"]


class GuidePatternSerializer(serializers.ModelSerializer):
    example_problems = GuideExampleProblemSerializer(many=True, read_only=True)

    class Meta:
        model = GuidePattern
        fields = [
            "name", "how_it_works", "diagram_svg", "recognition_signals", "code_solution",
            "code_language", "example_problems",
        ]


class ToolSerializer(serializers.ModelSerializer):
    skill_agent_entries = SkillAgentEntrySerializer(many=True, read_only=True)
    guide_patterns = GuidePatternSerializer(many=True, read_only=True)

    class Meta:
        model = Tool
        fields = [
            "id", "title", "slug", "category", "description", "url", "order",
            "created_at", "skill_agent_entries", "guide_patterns",
        ]
