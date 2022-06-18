from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers

from .models import Article, Category

from rest_framework.permissions import BasePermission
from datetime import timedelta, datetime
from django.utils import timezone

# custom permission class
class RegisteredMoreThanThreeDaysUser(BasePermission):
    """
    가입일 기준 3일 이상 지난 사용자만 접근 가능
    """
    message = '가입 후 3일 이상 지난 사용자만 사용하실 수 있습니다.'

    def has_permission(self, request, view):
        join_date = request.user.join_date
        now =  datetime.now().date()
        return bool(request.user and join_date - now > timedelta(days=3))


class UserArticle(APIView, RegisteredMoreThanThreeDaysUser):
    # 로그인 된 사용자와 가입일이 3일 이상 지난 사용자만 view 조회 가능
    permission_classes = [IsAuthenticated, RegisteredMoreThanThreeDaysUser]

    #유저가 작성한 기사들 조회
    def get(self, request):
        print(request.user)
        user = request.user
        my_articles = str(Article.objects.filter(author=user))
        print(user)
        print(my_articles)

        return Response({'my_articles': my_articles})
    
    #기사 작성
    def post(self, request):
        user = request.user
        title = request.data.get('title', '')
        category = request.data.get('category', '')
        content = request.data.get('content', '')
       
        try:
            category = Category.objects.get(name=category)
            if len(title) > 5 and len(content) > 20:
                my_article = Article.objects.create(
                    author=user,
                    title=title,
                    content=content
                )
                # You cannot directly add an object to ManyToManyField when creating an instance. 
                my_article.category.add(category)
                return Response({'message': "Article posted!"})
            
            elif len(title) < 5:
                return Response({'message': "Aritcle title must be longer!"})

            elif len(content) < 20:
                return Response({'message': "Aritcle content must be longer!"})
        
        except Category.DoesNotExist:
            return Response({'message': "Article must include a valid cateogry."})


# 7. custom permission class를 활용해 가입 후 3일 이상 지난 사용자만 게시글을 쓸 수 있도록 해주세요
# - 테스트 할 때에는 가입 후 3분 이상 지난 사용자가 게시글을 쓸 수 있게 해주세요
# - join_date는 datetime field로 만들어주세요