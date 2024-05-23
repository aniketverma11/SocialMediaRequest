
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['uuid', 'email', 'first_name', 'last_name', 'password']

    def validate(self, data):
        if User.objects.filter(email=data["email"].lower()).exists():
            raise serializers.ValidationError("User with this email {} already exists".format(data["email"]))

        return data

    def create(self, validated_data):
        # Set the username to the email
        validated_data['username'] = validated_data['email']
        # Use create_user to ensure the password is hashed
        user = User.objects.create_user(**validated_data)
        return user
    
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "uuid",
            "email",
            "mobile",
            "first_name",
            "last_name",
        ]


class LoginResponseSerializer(serializers.Serializer):
    user_profile = serializers.SerializerMethodField(read_only=True)
    refresh_token = serializers.CharField(read_only=True)
    access_token = serializers.CharField(read_only=True)

    def get_user_profile(self, profile):
        # Check the user_type field of the user_profile object
        if profile["user_profile"]:
            # If user_type is 10 (organization), serialize using OrganizationProfileSerializer
            return UserProfileSerializer(profile["user_profile"]).data

        else:
            return None
        

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims if needed
        # token['claim'] = value

        return token