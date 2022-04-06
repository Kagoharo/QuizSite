from django.contrib import admin
from .models import Quiz, Category, Question, Answer, UserAnswers


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Модель категорий для вывода в админ панели.
    """

    list_display = ('id', 'category_name', 'created_at')
    list_display_links = ('id', 'category_name')
    search_fields = ('category_name',)
    list_filter = ('created_at',)


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    """
    Модель опросов для вывода в админ панели.
    """

    list_display = ('id', 'quiz_name', 'category_id', 'created_at')
    list_display_links = ('id', 'quiz_name')
    search_fields = ('quiz_name',)
    list_filter = ('created_at', 'category_id')


class AnswerInline(admin.StackedInline):
    model = Answer
    min_num = 4
    extra = 0


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """
    Модель вопросов для вывода в админ панели.
    """

    inlines = [AnswerInline]
    list_display = ('id', 'question', 'quiz_id', 'created_at')
    list_display_links = ('id', 'question')
    search_fields = ('quiz_id',)
    list_filter = ('quiz_id', 'created_at')


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    """
    Модель ответов для вывода в админ панели.
    """

    list_display = ('id', 'answer', 'is_correct', 'question_id', 'created_at')
    list_display_links = ('id', 'answer')
    search_fields = ('answer', 'question_id')
    list_filter = ('is_correct', 'question_id', 'created_at')


@admin.register(UserAnswers)
class UserAnswersAdmin(admin.ModelAdmin):
    """
    Модель ответов пользователей для админ панели.
    """

    list_display = ('quiz_id', 'count_correct', 'answered_correct')
    list_filter = ('quiz_id', 'count_correct', 'answered_correct')
    search_fields = ('quiz_id', )
