from django.contrib import admin

# Register your models here.

from django.conf import settings
from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy as _

from .models import User


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("name", "email", "first_name", "last_name", "mobile")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ["uuid","username", "name",  "email", "first_name", "last_name","mobile", "is_superuser", "created"]
    search_fields = ["name", "uuid", "email"]