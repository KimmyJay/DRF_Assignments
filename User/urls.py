from django.contrib import admin
from django.urls import path, include
from User import views

urlpatterns = [
    path('', views.Login.as_view()),
    path('detail/', views.UserDetail.as_view()),

]