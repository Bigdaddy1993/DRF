from rest_framework.permissions import BasePermission


class IsModerator(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        is_authenticated = user.is_authenticated
        is_moderator = user.groups.filter(name="moderator").exists()
        return is_authenticated and is_moderator


class IsOwner(BasePermission):
    message = " не являетесь владельцем"

    def has_object_permission(self, request, view, obj):
        is_authenticated = request.user.is_authenticated
        is_owner = obj.owner == request.user
        return is_owner and is_authenticated
