from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import DetailView, TemplateView

from home import models


class ProfileView(LoginRequiredMixin, TemplateView):
    """
    Представление профиля пользователя.
    То есть тут выводится вся информация о пользователе, другими словами, профиль.
    """
    template_name = 'home/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
