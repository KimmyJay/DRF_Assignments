from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from django.contrib.auth import login, authenticate, logout

from User.serializers import UserSerializer

from User.models import CustomUser

class Login(APIView):
    permission_classes = [AllowAny] # 누구나 view 조회 가능
    # permission_classes = [IsAdminUser] # admin만 view 조회 가능
    # permission_classes = [IsAuthenticated] # 로그인 된 사용자만 view 조회 가능

    def post(self, request):
        username = request.data.get('username', '')
        password = request.data.get('password', '')

        user = authenticate(request, username=username, password=password)
        if not user:
            return Response({"error": "존재하지 않는 계정이거나 패스워드가 일치하지 않습니다."})

        login(request, user)
        return Response({"message": "로그인 성공!!"})

    def delete(self, request):
        logout(request)
        return Response({'message': '로그아웃 하셨습니다!'})


class UserDetail(APIView):
    def get(self, request):
        user = request.user
        return Response(UserSerializer(user).data)