from rest_framework import permissions


class IsLoggedInUserOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.is_staff


class IsLoggedInTeacherUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.user_type == 'TEACHER'


class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff

    def has_object_permission(self, request, view, obj):
        return request.user and request.user.is_staff


class IsLoggedInUserAndEventOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.teacher_user == request.user
