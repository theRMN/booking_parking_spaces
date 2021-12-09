from rest_framework import permissions


class IsManagerPermissionOrIsAdminUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.type == 'manager' or bool(request.user and request.user.is_staff)


class IsEmployeePermissionOrIsAdminUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.type == 'employee' or bool(request.user and request.user.is_staff)
