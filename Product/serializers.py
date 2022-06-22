from rest_framework import serializers
from User.models import *
from Product.models import *

from datetime import datetime, timedelta
from django.utils import timezone

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["author", "content", "rating"]

class ProductSerializer(serializers.ModelSerializer):    
    is_active = serializers.BooleanField(default=True)
    
    # 제일 최신 리뷰의 내용 불러오기
    review = serializers.SerializerMethodField()
    def get_review(self, obj):
        reviews = list(obj.review_set.values())
        if len(reviews) == 0:
            return "작성된 리뷰가 아직 없습니다"
        return reviews[-1]["content"]
        
    # 상품의 평균 평점 불러오기
    average_review = serializers.SerializerMethodField()
    def get_average_review(self, obj):
        product_reviews = obj.review_set.values()
        rating_list = [review['rating'] for review in product_reviews]
    
        if len(rating_list) == 0:
            average_rating = "평점 없음"
        else:    
            average_rating = round(sum(rating_list) / len(rating_list), 1)
        
        return average_rating
    
    def validate(self, data):
        http_method = self.context.get("request").method
        if http_method == "POST":
            if data.get("exposure_end_date") < datetime.now():
                raise serializers.ValidationError(
                    detail={"error": "이미 만료된 상품은 생성하실 수 없습니다"}
                )

        return data
    
    def create(self, validated_data):
        product = Product(**validated_data)
        product.save()
        product.description += f"  <{product.created} 에 등록된 상품입니다.>"
        product.save()
        
        return product
    
    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        # 수정이 안됐을 때
        if instance.updated == instance.created:
            instance.description = f"<{instance.updated} 에 수정됨> \n"+ instance.description
            instance.save()
        # 이미 수정했을 때
        else:
            print(instance.description)
            update_desc = instance.description.split("\\n")
            print(update_desc)
            desc="\n".join(update_desc[1:])
            print(desc)
            updated=f"<{instance.updated} 에 수정됨>\n" + desc
            print(updated)

            instance.description=updated
            instance.save()

        return instance
    
    class Meta:
        model = Product
        fields = ["seller", "title", "thumbnail", "description", 
                  "price", "average_review", "review", "is_active", 
                  "exposure_end_date", "exposure_start_date"]