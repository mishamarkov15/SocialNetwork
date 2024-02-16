from django.shortcuts import render
from django.views.generic import TemplateView

from friends.models import Friends
from messanger.models import Message


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
        user_id, friend_id = context['room_name'].split('t')
        if self.request.user.id == int(friend_id):
            user_id, friend_id = friend_id, user_id
        context['sender'] = Friends.objects.get(user_id=user_id, friend_id=friend_id)
        context['receiver'] = Friends.objects.get(user_id=friend_id, friend_id=user_id)

        context['message_history'] = Message.objects.filter(sender_id=user_id, receiver_id=friend_id).order_by(
            "sent_datetime") | \
                                     Message.objects.filter(receiver_id=user_id, sender_id=friend_id).order_by(
                                         "sent_datetime")

        print(f'history: {context["message_history"]}')
        return context
