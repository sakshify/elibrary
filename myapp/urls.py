from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('signup', views.signup,name="signup"),
    path('login', views.login,name="login"),
    path('addbook',views.addbook,name="addbook"),
    path('showbooks',views.showbook,name="showbooks"),
    path('main',views.main,name="main"),
    path('delete/<int:id>',views.delete,name="delete"),





]
