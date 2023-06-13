from rest_framework import permissions

class IsStaffOrAddOnly(permissions.BasePermission):
  
  def has_permission(self, request, view):
    if request.method == "POST":
      return True
    
    return bool(request.user and request.user.is_staff)