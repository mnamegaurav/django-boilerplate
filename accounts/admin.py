from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.utils.safestring import mark_safe

from accounts.models import UserGroup
from accounts.forms import CustomUserChangeForm, CustomUserCreationForm

User = get_user_model()

# Register your models here.

admin.site.unregister(Group)


@admin.register(UserGroup)
class UserGroupAdmin(GroupAdmin):
    pass


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = (
        "username",
        "mobile",
        "full_name",
        "email",
        "is_staff",
        "is_active",
        "is_superuser",
    )
    search_fields = (
        "username",
        "email",
        "mobile",
        "full_name",
    )
    list_editable = ("is_active",)
    ordering = ("mobile",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )
    actions = ["disable_selected_users", "enable_selected_users"]
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    add_fieldsets = (
        (
            None,
            {
                "fields": (
                    "full_name",
                    "username",
                    "mobile",
                    "email",
                    "photo",
                    "password1",
                    "password2",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "groups",
                )
            },
        ),
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "full_name",
                    "username",
                    "mobile",
                    "email",
                    "photo",
                    "current_avatar_image",
                    "password",
                )
            },
        ),
        ("Verification", {"fields": ("is_email_verified", "is_mobile_verified")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "groups",
                )
            },
        ),
    )
    readonly_fields = ("current_avatar_image",)

    @mark_safe
    def current_avatar_image(self, obj):
        return f'<img src="{obj.avatar_url}" height="80px" />'

    def disable_selected_users(self, request, queryset):
        queryset.update(is_active=False)

    disable_selected_users.short_description = "Disable selected users"

    def enable_selected_users(self, request, queryset):
        queryset.update(is_active=True)

    enable_selected_users.short_description = "Enable selected users"
