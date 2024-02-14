from django import forms


class FriendSearchForm(forms.Form):
    """
    Форма для поиска людей на странице с друзьями
    """
    to_search = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Введите имя или username пользователя',
    }))
