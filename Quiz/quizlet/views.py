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
    pk_url_kwarg = "pk"

    def get_context_data(self, **kwargs):
        context = super(QuizListView, self).get_context_data(**kwargs)
        pk = self.kwargs.get(self.pk_url_kwarg)
        context['quizzes'] = Quiz.objects.filter(category_id=pk)
        return context


class QuestionListView(ListView):
    """
    Вид списка вопросов.
    """

    model = Question
    template_name = 'question_list.html'
    context_object_name = 'questions'
    paginate_by = 5
    pk_url_kwarg = "pk"

    def get_context_data(self, **kwargs):
        context = super(QuestionListView, self).get_context_data(**kwargs)
        pk = self.kwargs.get(self.pk_url_kwarg)
        context['questions'] = Question.objects.filter(quiz_id=pk)
        context['answers'] = Answer.objects.filter(quiz_id=pk)
        return context
