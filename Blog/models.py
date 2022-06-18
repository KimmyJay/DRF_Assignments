from tkinter import CASCADE
from django.db import models
from User.models import CustomUser

# Create your models here.
class Category(models.Model):
    name = models.CharField("name", max_length=50)
    description = models.TextField("description", max_length=150)

class Article(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, related_name='article')
    title = models.CharField("title", max_length=50)
    content = models.TextField("description", max_length=500)

class Comment(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField("description", max_length=150)

