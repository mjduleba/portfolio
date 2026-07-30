from rest_framework import serializers
from .models import Hobby, UserProfile


class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobby
        fields = ["label", "icon_key"]


class ProfileSerializer(serializers.ModelSerializer):
    hobbies = HobbySerializer(many=True, read_only=True)

    class Meta:
        model = UserProfile
        fields = [
            "id",
            "name",
            "title",
            "bio",
            "email",
            "github_url",
            "linkedin_url",
            "leetcode_url",
            "location",
            "hobbies",
        ]
