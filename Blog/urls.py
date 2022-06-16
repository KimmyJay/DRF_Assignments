from django.contrib import admin
from django.urls import path
from Blog import views

urlpatterns = [
    path('', views.UserArticle.as_view()),


]