from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.views.generic.list import ListView
from .models import Quiz, Category
from .forms import CategoryForm


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


def category_create_view(request):
    """
    Вид списка категорий.
    """
    form = CategoryForm()
    context = {
        "form": form
    }
    if request.method == "POST":
        form = CategoryForm(request.POST)
        context['form'] = form
        if form.is_valid():
            category_name = form.cleaned_data.get('category_name')
            Category.objects.create(category_name=category_name)
            context['created'] = True
        return redirect('http://127.0.0.1:8000/quizzes')
    return render(request, "post_category.html", context=context)


class CategoryDetailView(ViewsMixin, DetailView):
    """
    Вид категории.
    """

    model = Category
    template_name = 'category.html'
    context_object_name = 'category'

    def get_title(self):
        return self.get_object().category_name + " опросы"


class QuizDetailView(ViewsMixin, DetailView):
    """
    Вид опроса.
    """

    model = Quiz
    template_name = 'quiz.html'
    context_object_name = 'quiz'

    def get_title(self):
        return self.get_object().quiz_name + " вопросы"
