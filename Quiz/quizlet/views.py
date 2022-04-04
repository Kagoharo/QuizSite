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


class CategoryMethodsViewsMixin:
    """
    Миксин для изменения и создания категорий.
    """
    create = None

    def get_success_url(self):
        return reverse('category_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(create=self.get_method())
        return context

    def get_method(self):
        return self.create


class QuizMethodsViewsMixin:
    """
    Миксин для изменения и создания опросов.
    """
    create = None

    def get_success_url(self):
        return reverse('quiz_list', kwargs={'pk': self.object.category_id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(create=self.get_method())
        return context

    def get_method(self):
        return self.create


class CategoryListView(ViewsMixin, ListView):
    """
    Вид списка категорий.
    """

    title = 'Категории опросов'

    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'


class CategoryCreateView(CategoryMethodsViewsMixin, CreateView):
    """
    Вид создания категории.
    """

    create = True

    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'


class CategoryUpdateView(CategoryMethodsViewsMixin, UpdateView):
    """
    Вид изменения категории.
    """

    create = False

    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'


class CategoryDetailView(ViewsMixin, DetailView):
    """
    Вид категории.
    """

    model = Category
    template_name = 'category_detail.html'
    context_object_name = 'category'

    def get_title(self):
        return self.get_object().category_name + " опросы"


class QuizCreateView(QuizMethodsViewsMixin, CreateView):
    """
    Вид создания опроса.
    """

    create = True

    model = Quiz
    form_class = QuizForm
    template_name = 'quiz_form.html'


class QuizUpdateView(QuizMethodsViewsMixin, UpdateView):
    """
    Вид изменения опроса.
    """

    create = False

    model = Quiz
    form_class = QuizForm
    template_name = 'quiz_form.html'


class QuizDetailView(ViewsMixin, DetailView):
    """
    Вид опроса.
    """

    model = Quiz
    template_name = 'quiz.html'
    context_object_name = 'quiz'

    def get_title(self):
        return self.get_object().quiz_name + " вопросы"
