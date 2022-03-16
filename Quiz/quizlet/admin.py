from django.contrib import admin
from .models import *


class AdminQuiz(admin.ModelAdmin):
    list_display = ('id', 'quiz_name', 'created_at')
    list_display_links = ('id', 'quiz_name')
    search_fields = ('quiz_name',)


class AdminCategory(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'quiz_id', 'created_at')
    list_display_links = ('id', 'category_name')
    search_fields = ('category_name', 'quiz_id')


class AdminQuestion(admin.ModelAdmin):
    list_display = ('id', 'question', 'quiz_id', 'category_id', 'created_at')
    list_display_links = ('id', 'question')
    search_fields = ('id', 'question', 'quiz_id', 'category_id')


class AdminAnswer(admin.ModelAdmin):
    list_display = ('id', 'answer', 'is_correct', 'question_id', 'created_at')
    list_display_links = ('id', 'answer')
    search_fields = ('answer', 'is_correct', 'question_id')


admin.site.register(Quiz, AdminQuiz)
admin.site.register(Category, AdminCategory)
admin.site.register(Question, AdminQuestion)
admin.site.register(Answer, AdminAnswer)
