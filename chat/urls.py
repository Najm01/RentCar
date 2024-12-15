from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_list, name='chat_list'),
    path('<int:chat_id>/', views.chat_detail, name='chat_detail'),
    path('create/<int:user_id>/', views.create_chat, name='create_chat'),
]
