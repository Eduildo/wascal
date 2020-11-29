# -*- encoding: utf-8 -*-
"""
Copyright (c) 2020 - Eduildo's.code
"""

from django.urls import path
from .import views
from django.contrib.auth.views import LogoutView

app_name = 'authentication'
urlpatterns = [
    #path('', views.index, name='index'),
    path('login_view/', views.login_view, name="login_view"),
    path('register_user', views.register_user, name="register_user"),
    path('new_candidat/', views.new_candidat, name='new_candidat'),
    #path("logout/", LogoutView.as_view(), name="logout")
]
