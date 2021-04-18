from rest_framework import serializers
from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ["email", "username", "password"]

    def validate(self, attrs):
        username = attrs.get("username", "")

        if not str(username).isalnum():
            raise serializers.ValidationError("username should be alphanumeric")
        return super().validate(attrs)

    def create(self, validated_data):
        return User.object.create_user(**validated_data)


class EmailValidationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = User
        fields = ["token"]
