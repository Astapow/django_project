from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsReadOnlyPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in ["GET", "HEAD", "OPTIONS"]:
            return True
        return False


class IsAdminOrReadOnlyPermission(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and request.user.is_superuser)
