from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db import models
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import DetailView
from django.views.generic.list import ListView
from .models import *


class QuizListView(ListView):
    model = Quiz
    template_name = 'quiz_list.html'
    context_object_name = 'quizzes'
    paginate_by = 100


class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'
    paginate_by = 100


class ShowQuiz(DetailView):
    model = Question
    template_name = 'question_list.html'
    context_object_name = 'questions'
    paginate_by = 100
    pk_url_kwarg = "Quiz_pk"
