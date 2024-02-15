from django import forms


class PostForm(forms.Form):
    """
    Форма для отправки поста
    """

    content = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Что у Вас нового?',
        'rows': 3,
        'cols': 80,
        'id': 'post-textarea',
    }))
