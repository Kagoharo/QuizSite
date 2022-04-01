from django.shortcuts import render, redirect
from django.views.generic import DetailView
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


def category_create_view(request):
    """
    Вид списка категорий.
    """
    form = CategoryForm()
    context = {"form": form}
    if request.method == "POST":
        form = CategoryForm(request.POST)
        context['form'] = form
        if form.is_valid():
            form.save()
        return redirect('http://127.0.0.1:8000/quizzes')
    return render(request, "category_form.html", context=context)


def category_update_view(request, pk):
    """
    Вид списка категорий.
    """
    category = Category.objects.get(id=pk)
    form = CategoryForm(instance=category)
    context = {"form": form}
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        context['form'] = form
        if form.is_valid():
            form.save()
        return redirect('http://127.0.0.1:8000/quizzes')
    return render(request, "category_form.html", context=context)


class CategoryDetailView(ViewsMixin, DetailView):
    """
    Вид категории.
    """

    model = Category
    template_name = 'category.html'
    context_object_name = 'category'

    def get_title(self):
        return self.get_object().category_name + " опросы"


def quiz_create_view(request, pk):
    """
    Вид списка категорий.
    """
    form = QuizForm()
    pk = pk
    url = 'http://127.0.0.1:8000/quizzes/category/' + str(pk)
    context = {"form": form}
    if request.method == "POST":
        form = QuizForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(url)
    return render(request, "quiz_form.html", context=context)


def quiz_update_view(request, pk):
    """
    Вид списка категорий.
    """
    url = 'http://127.0.0.1:8000/quizzes/category/' + str(pk)
    quiz = Quiz.objects.get(id=pk)
    form = QuizForm(instance=quiz)
    context = {"form": form}
    if request.method == "POST":
        form = QuizForm(request.POST, instance=quiz)
        context['form'] = form
        if form.is_valid():
            form.save()
        return redirect(url)
    return render(request, "quiz_form.html", context=context)


class QuizDetailView(ViewsMixin, DetailView):
    """
    Вид опроса.
    """

    model = Quiz
    template_name = 'quiz.html'
    context_object_name = 'quiz'

    def get_title(self):
        return self.get_object().quiz_name + " вопросы"
