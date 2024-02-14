from django.urls import path

from messanger.views import ChatsList

app_name = 'messanger'

urlpatterns = [
    path('', ChatsList.as_view(), name='chat-list')
]
