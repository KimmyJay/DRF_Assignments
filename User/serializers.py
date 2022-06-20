from rest_framework import serializers
from User.models import *
from Blog.models import *

from Blog.serializers import ArticleSerializer

class DishSerializer(serializers.ModelSerializer):
    # we can create a reverse lookup function inside a Serializer
    same_dish_users = serializers.SerializerMethodField()
    def get_same_dish_users(self, obj):
        print(obj.userprofile_set.all())
        return [up.user.realname for up in obj.userprofile_set.all()]

    class Meta:
        model = Dish
        fields = ["name", "same_dish_users"]

class UserProfileSerializer(serializers.ModelSerializer):        
    # note that Dish and UserProfile have a many-to-many relationship
    # if the input data is a QuerySet, we will need to add the parameter (many=True)
    favorite_dish = DishSerializer(many=True)
    class Meta:
        model = UserProfile
        fields = ["TMI", "age", "favorite_dish"]

class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer()
    article_set = ArticleSerializer(many=True)
    
    class Meta:
        model = CustomUser
        fields = ["username", "realname", "email", "join_date", "userprofile", "article_set"]