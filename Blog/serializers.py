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
    category = serializers.SerializerMethodField()
    comment_set = CommentSerializer(many=True)

    def get_category(self, obj):
        return [category.name for category in obj.category.all()]

    class Meta:
        model = Article
        fields = ["category", "title", "content", "comment_set"]