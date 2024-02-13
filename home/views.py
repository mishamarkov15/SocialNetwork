from django.shortcuts import render
from django.views.generic import DetailView, TemplateView

from home import models


class ProfileView(DetailView):
    """
    Представление профиля пользователя.
    То есть тут выводится вся информация о пользователе, другими словами, профиль.
    """

    template_name = 'home/profile.html'
    model = models.MyUser
    context_object_name = 'user'
