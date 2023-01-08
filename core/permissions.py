from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    Handles object level permissions for objects.
    """

    def has_object_permission(self, request, view, obj):

        # check if user is owner
        if obj.user:
            return bool(request.user == obj.user)
        return False
