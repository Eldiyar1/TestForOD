from rest_framework.permissions import BasePermission
from .models import Enterprise, Product


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        if isinstance(obj, Enterprise):
            return obj.user == request.user
        elif isinstance(obj, Product):
            return obj.enterprise.user == request.user

        return False
