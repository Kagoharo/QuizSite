from django.views.generic import DetailView
from django.views.generic.list import ListView
from .models import Quiz, Category, Question, Answer


class CategoryListView(ListView):
    """
    Вид списка категорий.
    """

    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'
    paginate_by = 5


class QuizListView(ListView):
    """
    Вид списка опросов.
    """

    model = Quiz
    template_name = 'quiz_list.html'
    context_object_name = 'quizzes'
    paginate_by = 5


class QuestionListView(ListView):
    """
    Вид списка вопросов.
    """

    model = Question
    template_name = 'question_list.html'
    context_object_name = 'questions'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(QuestionListView, self).get_context_data(**kwargs)
        context['answers'] = Answer.objects.all()
        return context

