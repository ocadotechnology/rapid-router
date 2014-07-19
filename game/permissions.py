from rest_framework import permissions

class UserIsStudent(permissions.BasePermission):
	def has_permission(self, request, view):
		return (hasattr(request.user, "userprofile") and
	            hasattr(request.user.userprofile, "student"))

class WorkspacePermissions(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		return (obj.owner == request.user.userprofile.student)