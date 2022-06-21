from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from rest_framework import status

from permissions import *

from Product.models import *

from Product.serializers import ProductSerializer

from datetime import timezone, datetime, timedelta

from django.db.models import Q

class ProductView(APIView):
    permission_classes = [IsAuthenticated]

    # 로그인한 유저가 작성한 만료되지 않은 상품들 조회
    def get(self, request):
        user = request.user
        now = datetime.now()

        my_products = list(Product.objects.filter(
            Q(author=user) |
            Q(end_date__gte = now) |
            Q(start_date__lte = now)).order_by('-created'))
      
        return Response(ProductSerializer(my_products, many=True).data)

    
    #상품 작성, validation 사용
    def post(self, request):
        user = request.user
        request.data['author'] = user.id

        product_serializer = ProductSerializer(data=request.data, context={"request": request})
        
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data, status=status.HTTP_200_OK)

        return Response(product_serializers.errors, status.HTTP_400_BAD_REQUEST) 
    
    #상품 수정
    def put(self, request, obj_id):
        user = request.user
        request.data["author"] = user.id
        product = Product.objects.get(id=obj_id)

        product_serializer = ProductSerializer(product, data=request.data, context={"request": request}, partial=True)

        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data, status=status.HTTP_200_OK)

        return Response(product_serializers.errors, status.HTTP_400_BAD_REQUEST) 