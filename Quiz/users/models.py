from django.db import models


class CustomUser(models.Model):
    """
    Модель пользователя
    """

    username = models.CharField(verbose_name='Имя пользователя', max_length=30)
    password = models.CharField(verbose_name='Пароль', max_length=30)
    email = models.EmailField(verbose_name='Электронная почта')

