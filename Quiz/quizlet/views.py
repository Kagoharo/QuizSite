from django.urls import reverse
from django.views.generic import DetailView, CreateView, UpdateView
from django.views.generic.list import ListView
from .models import Quiz, Category, UserAnswers
from .forms import CategoryForm, QuizForm, UserAnswerFormSet, UserAnswersForm


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


class CreateUpdateMixin:
    """
    Миксин для миксинов изменения и создания.
    """

    create = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(create=self.create)
        return context


class CategoryCreateUpdateMixin(CreateUpdateMixin):
    """
    Миксин для изменения и создания категорий.
    """

    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'

    def get_success_url(self):
        return reverse('category_list')


class QuizCreateUpdateMixin(CreateUpdateMixin):
    """
    Миксин для изменения и создания опросов.
    """

    model = Quiz
    form_class = QuizForm
    template_name = 'quiz_form.html'

    def get_success_url(self):
        return reverse('quiz_list', kwargs={'pk': self.object.category_id})


class CategoryListView(ViewsMixin, ListView):
    """
    Вид списка категорий.
    """

    title = 'Категории опросов'

    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'


class CategoryCreateView(CategoryCreateUpdateMixin, CreateView):
    """
    Вид создания категории.
    """

    create = True


class CategoryUpdateView(CategoryCreateUpdateMixin, UpdateView):
    """
    Вид изменения категории.
    """

    create = False


class CategoryDetailView(ViewsMixin, DetailView):
    """
    Вид категории.
    """

    model = Category
    template_name = 'category_detail.html'
    context_object_name = 'category'

    def get_title(self):
        return f'{self.get_object().category_name} опросы'


class QuizCreateView(QuizCreateUpdateMixin, CreateView):
    """
    Вид создания опроса.
    """

    create = True


class QuizUpdateView(QuizCreateUpdateMixin, UpdateView):
    """
    Вид изменения опроса.
    """

    create = False


class QuizDetailView(ViewsMixin, DetailView):
    """
    Вид опроса.
    """

    model = Quiz
    template_name = 'quiz.html'
    context_object_name = 'quiz'

    def get_title(self):
        return f'{self.get_object().quiz_name} вопросы'


class UserAnswerView(CreateView):
    """
    Вид для ответа на вопрос.
    """

    model = UserAnswers
    form_class = UserAnswersForm
    template_name = 'user_answer.html'
    context_object_name = 'user_answer'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formset'] = UserAnswerFormSet(instance=self.object)
        return context


