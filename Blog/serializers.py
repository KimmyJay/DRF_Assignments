from rest_framework import serializers

from User.models import *
from Blog.models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    def get_author(self, obj):
        return obj.author.realname

    class Meta:
        model = Comment
        fields = ["author", "content"]


class ArticleSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True, read_only=True)
    get_categories = serializers.ListField(required=False) # 프론트에서 list형식으로 데이터를 보내줄때 사용
    comments = CommentSerializer(many=True, source="comment_set", read_only=True)

    # 카테고리 이름 가져오는 메소드
    # def get_categories(self, obj):
    #     return [category.name for category in obj.category.all()]

    
    def validate(self, data):
        categories = data.get("get_categories", [])
    
        if len(data.get("title", "")) < 5 :
            raise serializers.ValidationError(
                detail={"error": "제목은 5글자 이상 적어주세요."}
            )
        if len(data.get("content", "")) < 20 :
            raise serializers.ValidationError(
                detail={"error": "내용은 20자 이상 적어주세요."}
            )
        if not categories:
            raise serializers.ValidationError(
                detail={"error": "카테고리를 선택 해주세요."}
            )
        for category_id in categories:
            if not Category.objects.filter(id=category_id).exists():
                raise serializers.ValidationError(
                detail={"error": "카테고리를 잘못 지정했습니다."}
            )

        return data

    def create(self, validated_data):
        # cannot assign many-to-many field directly
        get_categorys = validated_data.pop("get_categories")
        my_article = Article.objects.create(**validated_data)
        my_article.category.add(*get_categorys)

        return my_article

    def update(self, instance, validated_data):
        # cannot assign many-to-many field directly
        get_categorys = validated_data.pop("get_categories")

        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()

        instance.category.set(*get_categorys)
        return instance

    class Meta:
        model = Article
        fields = ["author", "title", "get_categories", "category", 
                  "content", "comments", "start_date", "end_date"]

        extra_kwargs = {
            # 'comments': {'write_only': True},
            # 'email': {
            #     'error_messages': {
            #         'required': '이메일을 입력해주세요',
            #         'invalid': '이메일 형식을 지켜주세요',
            #         'required': False
            #     }
            # }
        }