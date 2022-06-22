from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.exceptions import APIException
from rest_framework import status

from datetime import timedelta, datetime, timezone
from django.utils import timezone

class GenericAPIException(APIException):
    def __init__(self, status_code, detail=None, code=None):
        self.status_code=status_code
        super().__init__(detail=detail, code=code)

# custom permission classes
class RegisteredMoreThanThreeDaysUser(BasePermission):
    """
    가입일 기준 3일 이상 지난 사용자만 접근 가능
    """
    message = '가입 후 3일 이상 지난 사용자만 사용하실 수 있습니다.'

    def has_permission(self, request, view):
        join_date = request.user.join_date
        now = timezone.now()

        return bool(request.user and now - join_date >= timedelta(seconds=3))

class IsAdminOrIsAuthenticatedReadOnly(BasePermission):
    """
    admin 사용자, 혹은 가입 후 7일이 지난 사용자는 모든 request 가능,
    로그인 사용자는 조회만 가능
    """

    SAFE_METHODS = ('GET', )
    message = '접근 권한이 없습니다.'

    def has_permission(self, request, view):
        user = request.user
        join_date = request.user.join_date
        now =  datetime.now()

        seven_days_passed = bool(now - join_date >= timedelta(days=7))

        if not user.is_authenticated:
            response = {
                'detail': "서비스를 이용하기 위해 로그인 해주세요."
            }
            raise GenericAPIException(status_code=status.HTTP_401_UNAUTHORIZED, detail=response)

        if user.is_admin or seven_days_passed:
            return True

        elif user.is_authenticated and request.method in self.SAFE_METHODS:
            return True

        return False

class IsAdminOrThreeDaysPassedrOrReadOnly(BasePermission):
    """
    admin 사용자, 혹은 가입 후 3일이 지난 사용자는 모든 request 가능,
    비로그인 사용자는 조회만 가능
    """

    SAFE_METHODS = ('GET', )
    message = '접근 권한이 없습니다.'

    def has_permission(self, request, view):
        user = request.user
        
        if request.method in self.SAFE_METHODS:
            return True
            
        if not user.is_authenticated:
            response = {
                'detail': "서비스를 이용하기 위해 로그인 해주세요."
            }
            raise GenericAPIException(status_code=status.HTTP_401_UNAUTHORIZED, detail=response)
        
        join_date = request.user.join_date
        now =  datetime.now()

        three_days_passed = bool(now - join_date >= timedelta(days=3))
        
        if (user.is_authenticated and user.is_admin) or three_days_passed:
            return True

        return False