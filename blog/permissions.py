from rest_framework import permissions
import logging

logger = logging.getLogger(__name__)

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        logger.info('So should this')
        # 安全方法（GET、HEAD、OPTIONS）開放所有人
        if request.method in permissions.SAFE_METHODS:
            return True
        # 其他方法只允許作者自己操作
        return obj.author == request.user
