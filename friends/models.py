from django.db import models

from home.models import MyUser


class Friends(models.Model):
    """
    Модель с дружескими связями между пользователями.
    """

    class Meta:
        db_table = 'friends'
        verbose_name = 'Друг'
        verbose_name_plural = 'Друзья'

    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='user',
                             name='user', help_text='Тот КТО дружит')
    friend = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='friend',
                               name='friend', help_text='Тот с КЕМ дружит')
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата начала дружбы')

    def __str__(self) -> str:
        return f"{self.user.username}: {self.friend.username}"
