from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from django.views.generic import DetailView, TemplateView

from home import models
from home.forms import PostForm
from home.models import Post


class ProfileView(LoginRequiredMixin, TemplateView):
    """
    Представление профиля пользователя.
    То есть тут выводится вся информация о пользователе, другими словами, профиль.
    """
    template_name = 'home/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['form'] = PostForm()
        context['posts'] = Post.objects.filter(user_id=self.request.user)
        return context

    def post(self, request: WSGIRequest, *args, **kwargs):
        form = PostForm(request.POST)
        context = self.get_context_data()
        if form.is_valid():
            post = Post(
                user_id=self.request.user,
                content=form.cleaned_data['content']
            )
            post.save()
        else:
            context['form'] = form
        return render(self.request, self.template_name, context)

