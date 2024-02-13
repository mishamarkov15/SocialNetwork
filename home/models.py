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

    username = models.CharField(name='username', max_length=32, unique=True)
    email = models.EmailField(_("email address"), unique=True)
    joined_timestamp = models.DateTimeField(name='Время регистрации', auto_now_add=True)
    birth_date = models.DateField(name='Дата рождения', default=datetime.datetime.now)
    about = models.TextField(name='О себе', null=True, blank=True)
    gender = models.CharField(name='Пол', max_length=1, choices=GENDERS, default=GENDERS[0][0])

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email
