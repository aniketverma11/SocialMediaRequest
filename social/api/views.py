from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from django.db.models import Q

from users.models import User
from social.models import FriendRequest

from .serializers import FriendRequestSerializer, FrientRequestAcceptSerializer, FriendRequestSendSerializer
from users.api.serializers import UserSerializer


class FriendRequestView(APIView):
    def post(self, request):
        data = request.data
        serializer = FriendRequestSendSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            to_user_id = serializer.data["to_user_id"]
        to_user = User.objects.get(uuid=to_user_id)
        if FriendRequest.objects.filter(from_user=request.user, to_user=to_user).exists():
            return Response({'message': 'Friend request already sent'}, status=status.HTTP_400_BAD_REQUEST)
        FriendRequest.objects.create(from_user=request.user, to_user=to_user)
        return Response({'message': 'Friend request sent'}, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        data = request.data
        serializer = FrientRequestAcceptSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            action = serializer.data["action"]
        friend_request = FriendRequest.objects.get(uuid=pk)
        if action == 'accept':
            friend_request.status = 'accepted'
            friend_request.save()
        elif action == 'reject':
            friend_request.status = 'rejected'
            friend_request.save()
        return Response({'message': f'Friend request {action}ed'}, status=status.HTTP_200_OK)

class ListFriendsView(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(sent_requests__status='accepted', sent_requests__from_user=self.request.user)

class ListPendingRequestsView(generics.ListAPIView):
    serializer_class = FriendRequestSerializer

    def get_queryset(self):
        return FriendRequest.objects.filter(to_user=self.request.user, status='pending')