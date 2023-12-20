from rest_framework import serializers

from social_media.models import (
    UserProfile, Follow, Post, Comment, Like
)


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"


class UserProfileListSerializer(UserProfileSerializer):
    class Meta:
        model = UserProfile
        fields = ("id", "user_image", "full_name")


class UserProfileDetailSerializer(UserProfileSerializer):
    user_email = serializers.EmailField(
        source="user.email", read_only=True
    )
    followers_count = serializers.IntegerField(read_only=True)
    following_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = UserProfile
        fields = (
            "id",
            "user_image",
            "user_email",
            "nickname",
            "first_name",
            "last_name",
            "bio",
            "followers_count",
            "following_count",
        )


class UserProfileImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ("id", "user_image")
