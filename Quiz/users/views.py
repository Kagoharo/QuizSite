from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse

from .forms import LoginForm


class AuthView(LoginView):
    """
    Вид для аутентификации
    """

    form_class = LoginForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse('category_list')
