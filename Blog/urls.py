from django.contrib import admin
from django.urls import path
from Blog import views

urlpatterns = [
    path('', views.ArticleView.as_view()),
    path('<obj_id>', views.ArticleView.as_view()),

]