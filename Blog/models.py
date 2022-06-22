from tkinter import CASCADE
from django.db import models
from User.models import CustomUser
from datetime import timedelta, datetime

# Create your models here.
class Category(models.Model):
    name = models.CharField("name", max_length=50)
    description = models.TextField("description", max_length=150)

    def __str__(self):
        return self.name

class Article(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, related_name='article')
    title = models.CharField("title", max_length=50)
    content = models.TextField("content", max_length=500)
    created = models.DateTimeField("created", auto_now_add=True)
    start_date = models.DateTimeField(default=datetime.now)
    end_date = models.DateTimeField(default=datetime.now()+timedelta(days=5))

    def __str__(self):
        return "{}님의 {}기사입니다.".format(self.author, self.title)

class Comment(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField("content", max_length=150)

    # def __str__(self):
    #     return self.content

