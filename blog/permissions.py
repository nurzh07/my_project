from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Разрешение для того, чтобы только автор мог редактировать или удалять свои посты.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True  # Разрешаем все безопасные методы (GET, HEAD, OPTIONS)
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True  # Разрешаем безопасные методы для всех
        return obj.author == request.user  # Только автор может редактировать или удалять
