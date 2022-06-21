from rest_framework import serializers
from User.models import *
from Blog.models import *

# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ["name", "description"]


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    def get_author(self, obj):
        return obj.author.realname

    class Meta:
        model = Comment
        fields = ["author", "content"]


class ArticleSerializer(serializers.ModelSerializer):
    categories = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, source="comment_set", read_only=True)

    def get_categories(self, obj):
        return [category.name for category in obj.category.all()]


    def create(self, validated_data):
        Article.objects.create(**validated_data)
        return validated_data

    class Meta:
        model = Article
        fields = ["title", "categories", "content", "comments", "start_date", "end_date"]

        extra_kwargs = {
            'comments': {'write_only': True},
            'email': {
                'error_messages': {
                    'required': '이메일을 입력해주세요',
                    'invalid': '이메일 형식을 지켜주세요',
                    'required': False
                }
            }
        }