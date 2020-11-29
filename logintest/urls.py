from django.urls import path
from . import views

app_name = 'logintest'

urlpatterns = [
    path('', views.index, name='index'),
]