from django.db import models

from utils.behaviours import UUIDMixin, StatusMixin, UserStampedMixin

from users.models import User


class FriendRequest(UUIDMixin, StatusMixin, UserStampedMixin):
    from_user = models.ForeignKey(User, related_name='sent_requests', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='received_requests', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('from_user', 'to_user')
        verbose_name = "Friend Requests"
        verbose_name_plural = "Friend Requests"