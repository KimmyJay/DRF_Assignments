from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from Product.models import Product
from Product.serializers import ProductSerializer
from django.db.models import Q
from django.utils import timezone
from permissions import *
from rest_framework.permissions import AllowAny, IsAuthenticated

class ProductView(APIView):
    permission_classes = [IsAdminOrThreeDaysPassedrOrReadOnly]

    #상품 조회
    def get(self, request):
        user = request.user
        # 로그인된 유저의 만료되지 않은 상품들 queryset으로 가져오기
        if user.is_authenticated:
            my_products = Product.objects.filter(
                Q(exposure_end__gte=datetime.now())|
                Q(seller=user), 
                is_active=True
                )
            # json형태로 돌려주기
            product_serializer = ProductSerializer(my_products, many=True).data
        else:
            products = Product.objects.filter(
                Q(exposure_end__gte=datetime.now()), 
                is_active=True
                )
            product_serializer = ProductSerializer(products, many=True).data   
            
        return Response(product_serializer, status=status.HTTP_200_OK)
    
    #상품 등록
    def post(self, request):
        # 현재 로그인한 유저의 id를 seller로 지정
        user = request.user
        request.data['seller'] = user.id
        product_serializer = ProductSerializer(data=request.data, context={"request": request})
        
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data, status=status.HTTP_200_OK)
        
        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #상품 수정
    def put(self, request, obj_id):
        product = Product.objects.get(id=obj_id)
        product_serializer = ProductSerializer(product, data=request.data, partial=True, context={"request": request})
        
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data, status=status.HTTP_200_OK)
        
        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)