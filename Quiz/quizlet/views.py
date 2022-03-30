from django.views.generic import DetailView
from django.views.generic.list import ListView
from .models import Quiz, Category, Question, Answer


class ViewsMixin:
    paginate_by = 5

    def get_user_context(self, **kwargs):
        context = kwargs
        pk = self.kwargs.get(self.pk_url_kwarg)
        quizzes = Quiz.objects.filter(category_id=pk)
        context['quizzes'] = quizzes
        questions = Question.objects.filter(quiz_id=pk)
        context['questions'] = questions
        return context


class CategoryListView(ListView):
    """
    Вид списка категорий.
    """

    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'
    extra_context = {'title': 'Категории опросов'}


class QuizDetailView(ViewsMixin, DetailView):
    """
    Вид списка опросов.
    """

    model = Quiz
    template_name = 'quiz_list.html'
    context_object_name = 'quizzes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Опросы")
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class QuestionDetailView(ViewsMixin, DetailView):
    """
    Вид списка вопросов.
    """

    model = Question
    template_name = 'question_list.html'
    context_object_name = 'question'
    extra_context = {'title': 'Вопросы'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Вопросы")
        context = dict(list(context.items()) + list(c_def.items()))
        return context
