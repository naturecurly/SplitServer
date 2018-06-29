from django.contrib.auth.models import User
from rest_framework import serializers

from split.models import Profile, Relationship


class AuthUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=150, write_only=True)

    def create(self, validated_data):
        Profile(username=validated_data['username'],
                email=validated_data['email']).save()

        return User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password'],
        )

    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'email',
        )


class FriendSerializer(serializers.ModelSerializer):
    friend = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Relationship
        fields = (
            'friend',
            'is_pending',
        )


class ProfileSerializer(serializers.ModelSerializer):
    friends = FriendSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = (
            'username',
            'email',
            'friends',
        )
