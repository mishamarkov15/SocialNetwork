from django.shortcuts import render
from django.views.generic import TemplateView

from friends.models import Friends


class ChatsList(TemplateView):
    """
    Список чатов.
    """

    template_name = 'messanger/chat-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['chats'] = Friends.objects.filter(user_id=self.request.user.pk)
        return context


class Chat(TemplateView):
    """
    Комната чата с пользователем
    """

    template_name = 'messanger/room.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['room_name'] = self.request.GET.get('username', None)
        path = self.request.path_info
        if path.endswith('/'):
            path = path[:-1]
        context['room_name'] = path.split('/')[-1]
        context['receiver'] = Friends.objects.get(friend__username=context['room_name'])
        return context
