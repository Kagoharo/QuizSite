from django.views.generic import DetailView
from django.views.generic.list import ListView
from .models import Quiz, Category


class ViewsMixin:
    """
    Миксин.
    """

    title = None
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(title=self.get_title())
        return context

    def get_title(self):
        return self.title


class CategoryListView(ViewsMixin, ListView):
    """
    Вид списка категорий.
    """

    title = 'Категории опросов'

    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'


class CategoryDetailView(ViewsMixin, DetailView):
    """
    Вид категории.
    """

    title = " опросы"

    model = Category
    template_name = 'category.html'
    context_object_name = 'category'

    def get_title(self):
        return self.get_object().category_name + self.title


class QuizDetailView(ViewsMixin, DetailView):
    """
    Вид опроса.
    """

    title = " вопросы"

    model = Quiz
    template_name = 'quiz.html'
    context_object_name = 'quiz'

    def get_title(self):
        return self.get_object().quiz_name + self.title
