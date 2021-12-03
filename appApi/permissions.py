from rest_framework import permissions
from .models import User

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

class IsDoctor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.doctor == request.user


# class isActivePermission(permissions.BasePermission):
#     """
#     Global permission check for blocked IPs.
#     """

#     def has_permission(self, request, view):
#         blocked = User.objects.filter(is_active=True).exists()
#         return True