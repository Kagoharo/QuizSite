from django.shortcuts import render, redirect
from .forms import CategoryForm, QuizForm
from .models import Category, Quiz


def category_create_view(request):
    """
    Вид добавления категории.
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
    Вид изменения категории.
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


def quiz_create_view(request, pk):
    """
    Вид создания опроса.
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
    Вид изменения опроса.
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