from rest_framework import serializers

from social.models import FriendRequest
from users.api.serializers import UserSerializer


class FriendRequestSerializer(serializers.ModelSerializer):
    from_user = UserSerializer(read_only=True)
    to_user = UserSerializer(read_only=True)

    class Meta:
        model = FriendRequest
        fields = ['uuid', 'from_user', 'to_user', 'status', 'created_at']

class FrientRequestAcceptSerializer(serializers.Serializer):
    action = serializers.CharField()

class FriendRequestSendSerializer(serializers.Serializer):
    to_user_id = serializers.CharField()