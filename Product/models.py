import os
from tkinter import CASCADE
from django.conf import settings
from django.db import models
from User.models import CustomUser
from datetime import timedelta, datetime

from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

def images_path():
    return os.path.join(settings.LOCAL_FILE_DIR, 'images')

class Product(models.Model):
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField("title", max_length=50)
    description = models.TextField("description", max_length=500)
    thumbnail = models.FileField("thumbnail", upload_to="product/")
    created = models.DateTimeField("created", auto_now_add=True)
    updated = models.DateTimeField("updated", auto_now=True)
    exposure_start_date = models.DateTimeField("exposure_start_date", default=datetime.now)
    exposure_end_date = models.DateTimeField("exposure_end_date", default=datetime.now()+timedelta(days=6))
    price = models.DecimalField("price", default=0.00, max_digits=6, decimal_places=2)
    is_active = models.BooleanField("is_active", default=True)

    def __str__(self):
        return "{}님의 {}상품입니다.".format(self.seller, self.title)


class Review(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    content = models.TextField("content", max_length=500)
    rating = models.IntegerField(null=True, validators=[MinValueValidator(0), MaxValueValidator(5)])
    created = models.DateTimeField("created", auto_now_add=True)

    def __str__(self):
        return "{}가 {}상품에 남긴 리뷰입니다.".format(self.author, self.product)