from rest_framework import serializers
from account.models import User


UserModel = User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, write_only=True)

    def create(self, validated_data):
        email = validated_data["email"]

        user = UserModel.objects.create_user(
            email=email,
            name=validated_data["name"],
            password=validated_data["password"],
        )

        return user

    class Meta:
        model = User
        fields = ["name", "email", "password"]
