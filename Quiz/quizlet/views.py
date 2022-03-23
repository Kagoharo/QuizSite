from django.views.generic import DetailView
from django.views.generic.list import ListView
from .models import Quiz, Category, Question


class QuizListView(ListView):
    """
    Вид списка опросов.
    """

    model = Category
    template_name = 'quiz_list.html'
    context_object_name = 'quizzes'
    paginate_by = 100


class CategoryListView(ListView):
    """
    Вид списка категорий.
    """

    model = Quiz
    template_name = 'category_list.html'
    context_object_name = 'categories'
    paginate_by = 100


class ShowQuiz(DetailView):
    """
    Детальный вид опроса.
    """

    model = Question
    template_name = 'question_list.html'
    context_object_name = 'questions'
    paginate_by = 100
