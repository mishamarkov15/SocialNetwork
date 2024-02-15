import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

GENDERS = (
    ('М', 'Мужской'),
    ('Ж', 'Женский'),
)


class MyUser(AbstractUser):

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    first_name = models.CharField(max_length=50, default='Name')
    last_name = models.CharField(max_length=50, default='No')
    username = models.CharField(verbose_name='username', max_length=32, unique=True)
    email = models.EmailField(_("email address"), unique=True)
    joined_timestamp = models.DateTimeField(verbose_name='Время регистрации', auto_now_add=True)
    birth_date = models.DateField(verbose_name='Дата рождения', default=datetime.datetime.now)
    about = models.TextField(verbose_name='О себе', null=True, blank=True)
    gender = models.CharField(verbose_name='Пол', max_length=1, choices=GENDERS, default=GENDERS[0][0])

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        elif self.first_name:
            return self.first_name
        elif self.last_name:
            return self.last_name
        else:
            return "No Name"

    def get_age(self) -> int:
        if self.birth_date:
            return (datetime.date.today() - self.birth_date).days // 365
        else:
            return 0


class Post(models.Model):
    """
    Модель для поста на стене
    """

    class Meta:
        db_table = 'post'
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    user_id = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='publisher')
    content = models.TextField(max_length=4096, null=False)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    views = models.BigIntegerField(default=0)


class Like(models.Model):
    """
    Модель для оценки поста
    """

    class Meta:
        db_table = 'like'
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'

    user_id = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='user_liker')
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post')
    type = models.CharField(max_length=10, choices=(
        ('like', 'Нравится'),
        ('dislike', 'Не нравится'),
    ))
