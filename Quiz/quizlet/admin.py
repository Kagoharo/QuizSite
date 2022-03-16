from django.contrib import admin
from .models import Quiz, Category, Question, Answer


class AdminQuiz(admin.ModelAdmin):
    """
    Модель опросов для админа.
    """

    list_display = ('id', 'quiz_name', 'created_at')
    list_display_links = ('id', 'quiz_name')
    search_fields = ('quiz_name',)
    list_filter = ('created_at', )


class AdminCategory(admin.ModelAdmin):
    """
    Модель категорий для админа.
    """

    list_display = ('id', 'category_name', 'quiz_id', 'created_at')
    list_display_links = ('id', 'category_name')
    search_fields = ('category_name', 'quiz_id')
    list_filter = ('quiz_id', 'created_at')


class AdminQuestion(admin.ModelAdmin):
    """
    Модель вопросов для админа.
    """

    list_display = ('id', 'question', 'quiz_id', 'category_id', 'created_at')
    list_display_links = ('id', 'question')
    search_fields = ('quiz_id', 'category_id')
    list_filter = ('quiz_id', 'category_id', 'created_at')


class AdminAnswer(admin.ModelAdmin):
    """
    Модель ответов для админа.
    """

    list_display = ('id', 'answer', 'is_correct', 'question_id', 'created_at')
    list_display_links = ('id', 'answer')
    search_fields = ('answer', 'question_id')
    list_filter = ('is_correct', 'question_id', 'created_at')


admin.site.register(Quiz, AdminQuiz)
admin.site.register(Category, AdminCategory)
admin.site.register(Question, AdminQuestion)
admin.site.register(Answer, AdminAnswer)
