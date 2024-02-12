from django.shortcuts import render
from django.views.generic import DetailView, TemplateView


class ProfileView(TemplateView):
    """
    Представление профиля пользователя.
    То есть тут выводится вся информация о пользователе, другими словами, профиль.
    """

    template_name = 'home/profile.html'
