from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'token')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        token = Token.objects.create(user=user)
        user.token = token.key
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)

    def validate(self, data):
        user = authenticate(
            username=data.get("username"),
            password=data.get("password")
        )

        if not user:
            raise serializers.ValidationError("Invalid login credentials")

        token, created = Token.objects.get_or_create(user=user)
        return {
            "username": user.username,
            "token": token.key
        }