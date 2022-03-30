from django.views.generic import DetailView
from django.views.generic.list import ListView
from .models import Quiz, Category, Question


class ViewsMixin:
    """
    Миксин.
    """

    paginate_by = 5
    title = None

    def get_user_context(self, **kwargs):
        context = kwargs
        return context

    def get_title(self):
        return self.title


class CategoryListView(ListView):
    """
    Вид списка категорий.
    """

    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'
    extra_context = {"title": "Категории опросов"}


class CategoryDetailView(ViewsMixin, DetailView):
    """
    Вид списка опросов.
    """

    model = Category
    template_name = 'category.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get(self.pk_url_kwarg)
        quizzes = Quiz.objects.filter(category_id=pk)
        context['quizzes'] = quizzes
        context.update(title=self.get_title())
        return context

    def get_title(self):
        return self.get_object().category_name


class QuestionDetailView(ViewsMixin, DetailView):
    """
    Вид списка вопросов.
    """

    model = Quiz
    template_name = 'quiz.html'
    context_object_name = 'quiz'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get(self.pk_url_kwarg)
        questions = Question.objects.filter(quiz_id=pk)
        context['questions'] = questions
        context.update(title=self.get_title())
        return context

    def get_title(self):
        return self.get_object().quiz_name
