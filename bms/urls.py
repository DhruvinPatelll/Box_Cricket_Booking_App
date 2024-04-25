from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home, name="home"),
    path("login/", views.Login, name="login"),
    path("register/", views.Register, name="register"),
    path("ground-detail/<slug:ground_slug>/", views.ground_detail, name="ground_detail"),
    path("success_page", views.Payment, name="success_page"),
    path("logout/", views.Logout, name="logout"),  
]
