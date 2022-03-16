from django.db import models


class AbstractQuizPattern(models.Model):
    """
    Общий шаблон для всех моделей.
    """

    created_at = models.DateField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateField(verbose_name='Дата обновления', auto_now=True)

    class Meta:
        abstract = True
        ordering = ('created_at',)


class Quiz(AbstractQuizPattern):
    """
    Модель опросов.
    """

    quiz_name = models.CharField(verbose_name='Название опроса', max_length=150)

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



class Category(AbstractQuizPattern):
    """
    Модель категории вопросов.
    """

    category_name = models.CharField(verbose_name='Название категории', max_length=150)
    quiz = models.ForeignKey(Quiz, related_name='quiz_categories', on_delete=models.CASCADE)

    class Meta(AbstractQuizPattern.Meta):
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return self.category_name


class Question(AbstractQuizPattern):
    """
    Модель вопросов.
    """

    quiz = models.ForeignKey(Quiz, related_name='quiz_questions', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='categories', on_delete=models.CASCADE)
    question = models.CharField(verbose_name='Вопрос', max_length=150)
    marks = models.IntegerField(verbose_name='Отметка', default=5)

    class Meta(AbstractQuizPattern.Meta):
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self) -> str:
        return self.question

    def get_answers(self):
        """
        Получение ответов связанных с вопросом.
        """

        return self.question_answers.all()


class Answer(AbstractQuizPattern):
    """
    Модель ответов.
    """

    question = models.ForeignKey(Question, related_name='question_answers', on_delete=models.CASCADE)
    answer = models.CharField(verbose_name='Ответ', max_length=150)
    is_correct = models.BooleanField(verbose_name='Правильность', default=False)

    class Meta(AbstractQuizPattern.Meta):
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self) -> str:
        return self.answer
