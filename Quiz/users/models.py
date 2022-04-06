from django.db import models


class CustomUser(models.Model):
    """
    Модель пользователя
    """

    username = models.CharField(verbose_name='Имя пользователя', max_length=30, unique=True)
    password = models.CharField(verbose_name='Пароль', max_length=30)
    email = models.EmailField(verbose_name='Электронная почта', unique=True)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password', 'email']
