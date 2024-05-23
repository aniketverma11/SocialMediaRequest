from django.contrib import admin
from .models import FriendRequest

class FriendRequestAdmin(admin.ModelAdmin):
    list_display = ('uuid','from_user', 'to_user', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('from_user__username', 'to_user__username')
    readonly_fields = ('created_at',)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.select_related('from_user', 'to_user')
        return queryset

admin.site.register(FriendRequest, FriendRequestAdmin)