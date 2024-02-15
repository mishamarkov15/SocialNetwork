from django.urls import path

from messanger.views import ChatsList, Chat

app_name = 'messanger'

urlpatterns = [
    path('', ChatsList.as_view(), name='chat-list'),
    path('<str:room_name>/', Chat.as_view(), name='chat'),
]
