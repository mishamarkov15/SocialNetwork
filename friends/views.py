from django.shortcuts import render
from django.views.generic import ListView, DetailView

from friends.models import Friends
from home.models import MyUser


class FriendListView(ListView):
    """
    Список друзей для текущего пользователя.
    """

    template_name = 'friends/friend_list.html'
    model = Friends
    context_object_name = 'friends'

    def get_queryset(self):
        return super().get_queryset().filter(user__pk=self.request.user.pk)


class UserProfileView(DetailView):
    """
    Страница пользователя нашей социальной сети (НЕ профиль).
    """

    template_name = 'friends/user_profile.html'
    model = MyUser
    context_object_name = 'user'
