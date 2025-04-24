from rest_framework import permissions
import logging

logger = logging.getLogger(__name__)

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # 安全方法（GET、HEAD、OPTIONS）開放所有人
        if request.method in permissions.SAFE_METHODS:
            return True
        # 其他方法只允許作者自己操作
        return obj.author == request.user

class IsStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        logger.info('has_permission called')
        logger.info(f'request:{request}')
        logger.info(f'request.user:{request.user}')
        logger.info(f'view:{view}')
        return True
    
    def has_object_permission(self, request, view, obj):
        logger.info('has_object_permission called')
        logger.info(f'request:{request}')
        logger.info(f'view:{view}')
        logger.info(f'obj:{obj}')
        return False