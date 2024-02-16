from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from friends import forms
from friends.forms import FriendSearchForm
from friends.models import Friends
from home.models import MyUser


class FriendListView(ListView):
    """
    Список друзей для текущего пользователя.
    """

    template_name = 'friends/friend_list.html'
    model = Friends
    context_object_name = 'friends'

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data(**kwargs)
        form = forms.FriendSearchForm(self.request.GET)
        context['form'] = form
        if form.is_valid() and form.cleaned_data['to_search']:
            context['new_users'] = MyUser.objects.filter(username__contains=form.cleaned_data['to_search']) | \
                                   MyUser.objects.filter(first_name__contains=form.cleaned_data['to_search']) | \
                                   MyUser.objects.filter(last_name__contains=form.cleaned_data['to_search'])
        return render(self.request, self.template_name, context)

    def get_queryset(self):
        form = forms.FriendSearchForm(self.request.GET)
        if form.is_valid() and form.cleaned_data['to_search']:
            return super().get_queryset().filter(user__pk=self.request.user.pk,
                                                 friend__username__contains=form.cleaned_data['to_search']) | \
                super().get_queryset().filter(user__pk=self.request.user.pk,
                                              friend__first_name__contains=form.cleaned_data['to_search']) | \
                super().get_queryset().filter(user__pk=self.request.user.pk,
                                              friend__last_name__contains=form.cleaned_data['to_search'])
        else:
            return super().get_queryset().filter(user__pk=self.request.user.pk)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = FriendSearchForm()
        return context


class UserProfileView(DetailView):
    """
    Страница пользователя нашей социальной сети (НЕ профиль).
    """

    template_name = 'friends/user_profile.html'
    model = MyUser
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['is_friend'] = Friends.objects.get(
                user_id=self.request.user.id,
                friend_id=self.object.id
            )
        except Exception as err:
            context['is_friend'] = None
        return context

    def post(self, request: WSGIRequest, *args, **kwargs):
        self.object = self.get_object()
        btn = self.request.POST.get('btn', None)
        if btn:
            if btn == 'delete':
                Friends.objects.get(
                    user=MyUser.objects.get(id=self.request.user.pk),
                    friend=MyUser.objects.get(id=self.object.id)
                ).delete()
                Friends(
                    friend=MyUser.objects.get(id=self.request.user.pk),
                    user=MyUser.objects.get(id=self.object.id)
                ).delete()
            elif btn == 'add':
                Friends(
                    user=MyUser.objects.get(id=self.request.user.pk),
                    friend=MyUser.objects.get(id=self.object.id)
                ).save()
                Friends(
                    friend=MyUser.objects.get(id=self.request.user.pk),
                    user=MyUser.objects.get(id=self.object.id)
                ).save()
        return render(self.request, self.template_name, self.get_context_data(**kwargs))
