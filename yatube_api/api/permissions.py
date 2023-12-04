from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Разрешение редактировать запись только автору."""

    def has_object_permission(self, request, view, obj):
        """Разрешение редактировать запись только автору."""
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )

    def has_permission(self, request, view):
        """Разррешение доступа только авторизованному пользователю."""
        return request.user.is_authenticated
