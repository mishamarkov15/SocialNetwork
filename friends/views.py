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
        return render(self.request, self.template_name, context)

    def get_queryset(self):
        form = forms.FriendSearchForm(self.request.GET)
        if form.is_valid() and form.cleaned_data['to_search']:
            print('found_form query')
            return super().get_queryset().filter(user__pk=self.request.user.pk,
                                                 friend__pk=form.cleaned_data['to_search'])
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
