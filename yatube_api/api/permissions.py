from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Кастомные разрешения для пользователей."""

    def has_object_permission(self, request, view, obj):
        """Проверка прав пользователя на объект."""
        return obj.author == request.user
