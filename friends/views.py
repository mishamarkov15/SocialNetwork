from django.shortcuts import render
from django.views.generic import ListView

from friends import models


class FriendListView(ListView):
    """
    Список друзей для текущего пользователя.
    """

    template_name = 'friends/friend_list.html'
    model = models.Friends
    context_object_name = 'friends'

    def get_queryset(self):
        return super().get_queryset().filter(user__pk=self.request.user.pk)
