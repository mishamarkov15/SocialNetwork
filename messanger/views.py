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
