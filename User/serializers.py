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
    userprofile = UserProfileSerializer(read_only=True)
    articles = ArticleSerializer(many=True, source="article_set", read_only=True)
    
    class Meta:
        model = CustomUser
        fields = ["username", "password", "realname", "email", "join_date", "userprofile", "articles"]

        # 유저 정보 조회할시 비밀번호는 숨김
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {
                'error_messages': {
                    'required': '이메일을 입력해주세요',
                    'invalid': '이메일 형식을 지켜주세요',
                    'required': False
                }
            }
        }