from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from .models import Article

class UserArticle(APIView):
 
    permission_classes = [permissions.IsAuthenticated] # 로그인 된 사용자만 view 조회 가능

    def get(self, request):
        user = request.user
        my_articles = str(Article.objects.filter(author=user))
        print(user)
        print(my_articles)

        return Response({'my_articles': my_articles})
