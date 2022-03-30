from django.db import models
from .managers import QuestionManager, QuizManager


class AbstractQuizPattern(models.Model):
    """
    Общий шаблон для всех моделей в models.py.
    """

    created_at = models.DateField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateField(verbose_name='Дата обновления', auto_now=True)

    class Meta:
        abstract = True
        ordering = ('created_at',)


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
