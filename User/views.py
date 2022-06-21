from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.hashers import make_password

from django.contrib.auth import login, authenticate, logout

from User.serializers import UserSerializer

from User.models import CustomUser

class User(APIView):
    permission_classes = [AllowAny] # 누구나 view 조회 가능
    # permission_classes = [IsAdminUser] # admin만 view 조회 가능
    # permission_classes = [IsAuthenticated] # 로그인 된 사용자만 view 조회 가능
    
    #사용자 정보 조회
    def get(self, request):
        user_serializer = UserSerializer(request.user, context={"request": request}).data
        return Response(user_serializer, status=status.HTTP_200_OK)
    
    #회원가입
    def post(self, request):
        password = request.data.get('password')
        request.data['password'] = make_password(password)
        user_serializer = UserSerializer(data=request.data)

        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_200_OK)

        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #회원 정보 수정
    def put(self, request):
        user = request.user
        user_serializer = UserSerializer(user, context={"request": request})
        return Response(user_serializer, status=status.HTTP_200_OK)
    #회원 탈퇴
    def delete(self, request):
        user_serializer = UserSerializer(request.user, context={"request": request})
        return Response(user_serializer, status=status.HTTP_200_OK)




class Login(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        user_serializer = UserSerializer(data=request.user)
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

