from django.db import models

from home.models import MyUser


class Message(models.Model):
    """
    Модель для объекта «сообщение».
    """
    class Meta:
        db_table = 'message'
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    sender_id = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='sender')
    receiver_id = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='receiver')
    title = models.CharField(max_length=250, verbose_name='Предпросмотр')
    content = models.TextField(max_length=4096, verbose_name='Контент')
    sent_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Время отправки')
    status = models.CharField(max_length=20, choices=(
        ('sent', 'отправлено'),
        ('delivered', 'доставлено'),
        ('seen', 'прочитано'),
        ('not_sent', 'не отправлено'),
    ))
