# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.chatpage, name='index'),
]