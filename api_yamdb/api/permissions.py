from rest_framework import permissions


class IsAdminOrSuperUser(permissions.BasePermission):
    """Права доступа для аутентифицированных пользователей
    со статусом администратора или суперюзера."""

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and request.user.is_admin
            or request.user.is_superuser)


class IsAdminOrReadOnly(permissions.IsAdminUser):
    """Права доступа для аутентифицированных пользователей
    со статусом администратора или для чтения."""

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            and request.user.is_admin
        )


class IsUserAdminModeratorOrReadOnly(permissions.BasePermission):
    """Права доступа для аутентифицированных пользователей
    со статусом администратора, автора или модератора."""

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
            or request.user.is_admin
            or request.user.is_moderator
        )
