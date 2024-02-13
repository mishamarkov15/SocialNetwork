from django.urls import path

from friends import views

app_name = 'friends'

urlpatterns = [
    path('', views.FriendListView.as_view(), name='friends-list')
]
