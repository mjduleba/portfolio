from rest_framework import serializers
from .models import Project, ProjectBullet


class ProjectBulletSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectBullet
        fields = ["text", "tags"]


class ProjectSerializer(serializers.ModelSerializer):
    bullets = ProjectBulletSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = [
            "id", "title", "description", "tech_stack", "github_url",
            "demo_url", "video_url", "image_url", "featured", "order",
            "created_at", "bullets",
        ]
