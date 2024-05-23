from django.urls import path
from social.api.views import FriendRequestView, ListFriendsView, ListPendingRequestsView

urlpatterns = [
    path('friend-request/', FriendRequestView.as_view(), name='friend_request'),
    path('friend-request/<uuid:pk>/', FriendRequestView.as_view(), name='update_friend_request'),
    path('friends/', ListFriendsView.as_view(), name='friends'),
    path('pending-requests/', ListPendingRequestsView.as_view(), name='pending_requests'),
]