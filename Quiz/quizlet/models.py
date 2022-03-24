from django.db import models
from django.db.models import Case, When, Count, F


class AbstractQuizPattern(models.Model):
    """
    Общий шаблон для всех моделей в models.py.
    """

    created_at = models.DateField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateField(verbose_name='Дата обновления', auto_now=True)

    class Meta:
        abstract = True
        ordering = ('created_at',)


class QuizManager(models.Manager):
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
        return self.filter(quiz_answers__is_correct=True).annotate(correct_answer=F("quiz_answers__answer"))


class QuestionManager(models.Manager):
    """
    Кастомный менеджер для вопросов.
    """

    def is_many_answers(self):
        """
        Аннотация для количества ответов к вопросу, много ли их.
        """
        return self.annotate(counter=Count('question_answers__answer'), meme=Case(When(counter__gte=3, then=True), default=False))


class Category(AbstractQuizPattern):
    """
    Модель категории вопросов.
    """

    category_name = models.CharField(verbose_name='Название категории', max_length=150)

    class Meta(AbstractQuizPattern.Meta):
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return self.category_name


class Quiz(AbstractQuizPattern):
    """
    Модель опросов.
    """

    quiz_name = models.CharField(verbose_name='Название опроса', max_length=150)
    category = models.ForeignKey(Category, verbose_name='ID категории', related_name='category_quizzes', default=1, on_delete=models.CASCADE)
    objects = QuizManager()

    class Meta(AbstractQuizPattern.Meta):
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

    def __str__(self) -> str:
        return self.quiz_name

    def get_questions(self):
        """
        Получение вопросов связанных с опросом.
        """
        return self.quiz_questions.all()


class QuizAnnotation(models.Model):
    """
    Модель опроса с аннотацией.
    """

    quiz = models.ForeignKey(Quiz, related_name='quiz_annotation', verbose_name='Аннотация опроса', on_delete=models.CASCADE)


class Question(AbstractQuizPattern):
    """
    Модель вопросов.
    """

    quiz = models.ForeignKey(Quiz, verbose_name='ID опроса', related_name='quiz_questions', default=1, on_delete=models.CASCADE)
    question = models.CharField(verbose_name='Вопрос', max_length=150)
    marks = models.IntegerField(verbose_name='Отметка', default=5)

    objects = QuestionManager()

    class Meta(AbstractQuizPattern.Meta):
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self) -> str:
        return self.question

    def get_answers(self):
        """
        Получение вопросв связанных с опросом.
        """
        return self.question_answers.all()


class QuestionAnnotation(models.Model):
    """
    Модель вопроса с аннотацией.
    """

    question = models.ForeignKey(Question, related_name='question_annotation', verbose_name='Аннотация вопроса', on_delete=models.CASCADE)


class Answer(AbstractQuizPattern):
    """
    Модель ответов.
    """

    question = models.ForeignKey(Question, verbose_name='ID вопроса', related_name='question_answers', default=1, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, default=1, related_name='quiz_answers', on_delete=models.CASCADE)
    answer = models.CharField(verbose_name='Ответ', max_length=150)
    is_correct = models.BooleanField(verbose_name='Правильность', default=False)

    class Meta(AbstractQuizPattern.Meta):
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self) -> str:
        return self.answer
