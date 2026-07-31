from rest_framework import serializers
from .models import Experience, ExperienceBullet


class ExperienceBulletSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienceBullet
        fields = ["text", "tags"]


class ExperienceSerializer(serializers.ModelSerializer):
    bullets = ExperienceBulletSerializer(many=True, read_only=True)

    class Meta:
        model = Experience
        fields = ["id", "role", "company", "company_icon_key", "location", "start_date", "end_date", "bullets"]
