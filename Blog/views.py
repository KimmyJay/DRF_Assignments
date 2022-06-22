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
        request.data['author'] = user.id

        # categorys = request.data.get('category', [])
        article_serializer = ArticleSerializer(data=request.data, context={"request": request})
        
        if article_serializer.is_valid(): # True or False 데이터가 유효한지 검사 
            article_serializer.save()
            return Response(article_serializer.data, status=status.HTTP_200_OK)
        
        return Response(article_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    

    #게시글 수정
    def put(self, request, obj_id):
        article = Article.objects.get(id=obj_id)
        # set partial=True to indicate we are editing only some fields
        article_serializer = ArticleSerializer(article, data=request.data, partial=True, context={"request": request})
        if article_serializer.is_valid():
            article_serializer.save()
            return Response(article_serializer.data, status=status.HTTP_200_OK)
    
        return Response(article_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    #게시글 삭제
    def delete(self, request, obj_id):
        article = Article.objects.get(id=obj_id)
        aritlcle.remove()
        return Response({"message": "게시글 삭제!!"})
    