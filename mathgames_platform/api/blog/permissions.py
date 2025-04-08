from rest_framework import permissions


class OwnerOrReadOnly(permissions.BasePermission):
    """
    Any who use safe method or not anon can get data,
    and only not anon or author can modificate.
    """

    def has_permission(self, request, view):

        return (request.method in permissions.SAFE_METHODS or
                request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS or
                obj.author == request.user)
