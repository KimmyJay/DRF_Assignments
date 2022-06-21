from rest_framework import serializers
from User.models import *
from Product.models import *

class ProductSerializer(serializers.ModelSerializer):
    
    def validate(self, data):
        if self.context.get("request").method == 'POST':
            return data
        if self.context.get("request").method == 'PUT':
            return data

    def create(self, validated_data):
        Product.objects.create(**validated_data)
        return validated_data

    def update(self, product, validated_data):
        for key, value in validated_data.items():
            setattr(product, key, value)
        product.save()

        return product

    class Meta:
        model = Product
        fields = ["author", "title", "description", "thumbnail", 
                  "created", "start_date", "end_date"]

        # extra_kwargs = {
            # 'comments': {'write_only': True},
            # 'email': {
            #     'error_messages': {
            #         'required': '이메일을 입력해주세요',
            #         'invalid': '이메일 형식을 지켜주세요',
            #         'required': False
            #     }
            # }
        # }