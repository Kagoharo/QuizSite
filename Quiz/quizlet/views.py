from django.views.generic import DetailView
from django.views.generic.list import ListView
from .models import Quiz, Category, Question


class ViewsMixin:
    """
    Миксин.
    """

    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get(self.pk_url_kwarg)
        questions = Question.objects.filter(quiz_id=pk)
        context['questions'] = questions
        quizzes = Quiz.objects.filter(category_id=pk)
        context['quizzes'] = quizzes
        context.update(title=self.get_title())
        return context


class CategoryListView(ListView):
    """
    Вид списка категорий.
    """

    title = 'Категории опросов'
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(title=self.get_title())
        return context

    def get_title(self):
        return self.title


class CategoryDetailView(ViewsMixin, DetailView):
    """
    Вид списка опросов.
    """

    model = Category
    template_name = 'category.html'
    context_object_name = 'category'

    def get_title(self):
        return self.get_object().category_name+' '+'опросы'


class QuestionDetailView(ViewsMixin, DetailView):
    """
    Вид списка вопросов.
    """

    model = Quiz
    template_name = 'quiz.html'
    context_object_name = 'quiz'

    def get_title(self):
        return self.get_object().quiz_name+' '+'тест'
