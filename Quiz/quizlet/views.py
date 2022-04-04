from django.urls import reverse
from django.views.generic import DetailView, CreateView, UpdateView
from django.views.generic.list import ListView
from .models import Quiz, Category
from .forms import CategoryForm, QuizForm


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


class CategoryCreateView(CreateView):
    """
    Вид создания категории.
    """

    model = Category
    form_class = CategoryForm
    template_name = 'category_create_form.html'

    def get_success_url(self):
        return reverse('category_list')


class CategoryUpdateView(UpdateView):
    """
    Вид изменения категории.
    """

    model = Category
    form_class = CategoryForm
    template_name = 'category_update_form.html'

    def get_success_url(self):
        return reverse('category_list')


class CategoryDetailView(ViewsMixin, DetailView):
    """
    Вид категории.
    """

    model = Category
    template_name = 'category_detail.html'
    context_object_name = 'category'

    def get_title(self):
        return self.get_object().category_name + " опросы"


class QuizCreateView(CreateView):
    """
    Вид создания опроса.
    """

    model = Quiz
    form_class = QuizForm
    template_name = 'quiz_create_form.html'

    def get_success_url(self):
        return reverse('quiz_list', kwargs={'pk': self.object.category_id})


class QuizUpdateView(UpdateView):
    """
    Вид изменения опроса.
    """

    model = Quiz
    form_class = QuizForm
    template_name = 'quiz_update_form.html'

    def get_success_url(self):
        return reverse('quiz_list', kwargs={'pk': self.object.category_id})


class QuizDetailView(ViewsMixin, DetailView):
    """
    Вид опроса.
    """

    model = Quiz
    template_name = 'quiz.html'
    context_object_name = 'quiz'

    def get_title(self):
        return self.get_object().quiz_name + " вопросы"
