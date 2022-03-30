from django.db import models
from django.db.models import Case, When, Count, F, Value


class QuizManager(models.QuerySet):
    """
    Кастомный менеджер для опросов.
    """

    def category_name_annotation(self):
        """
        Аннотация для названия категории.
        """
        return self.annotate(category_name_of_quiz=F('category__category_name'))

    def count_questions(self):
        """
        Аннотация для количества вопросов.
        """
        return self.annotate(count_questions=Count('quiz_questions'))

    def correct_answer_text(self):
        """
        Аннотация для правильного ответа.
        """
        return self.annotate(correct_answer=(Case(When(quiz_questions__question_answers__is_correct='True', then=Value('quiz_questions__question_answers__is_correct'))))).value_list('quiz_questions__question_answers__answer', 'quiz_questions__question_answers__is_correct')


class QuestionManager(models.QuerySet):
    """
    Кастомный менеджер для вопросов.
    """

    def has_many_answers(self):
        """
        Аннотация для количества ответов к вопросу, много ли их.
        """
        return self.annotate(counter=Count('question_answers__answer'), many_answers=Case(When(counter__gte=3, then=True), default=False))