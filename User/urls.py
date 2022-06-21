from django.contrib import admin
from django.urls import path, include
from User import views

urlpatterns = [
    path('login/', views.Login.as_view()),
    path('logout/', views.Login.as_view()),
    path('', views.User.as_view()),

]