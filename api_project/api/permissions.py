# api/permissions.py

from rest_framework.permissions import BasePermission

class IsBookOwner(BasePermission):
    """
    Custom permission to only allow owners of a book to edit it.
    """
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user  # Check if the user is the owner of the book