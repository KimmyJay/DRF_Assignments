from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers

from permissions import *

from Blog.models import Article, Category

from Blog.serializers import ArticleSerializer

from datetime import timezone, datetime, timedelta

class ArticleView(APIView):
    permission_classes = [IsAdminOrIsAuthenticatedReadOnly]

    # 로그인한 유저가 작성한 만료되지 않은 기사들 조회
    def get(self, request):
        user = request.user
        now = datetime.now()

        my_articles = list(Product.objects.filter(
            Q(author=user) |
            Q(end_date__gte = now) |
            Q(start_date__lte = now)).order_by('-start_date'))
            
        return Response(ArticleSerializer(my_articles, many=True).data)


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
            return Response({'message': "Article must include a valid category."})