from django.forms import ModelForm, inlineformset_factory
from .models import Category, Quiz, Answer, Question


class CategoryForm(ModelForm):
    """
    Форма для категории
    """

    class Meta:
        model = Category
        fields = '__all__'


class QuizForm(ModelForm):
    """
    Форма для опроса.
    """

    class Meta:
        model = Quiz
        fields = '__all__'


class QuestionForm(ModelForm):
    """
    Форма для вопросов.
    """

    class Meta:
        model = Question
        fields = '__all__'


QuizFormSet = inlineformset_factory(
    Quiz, Question, form = QuizForm,
    fields = ['question'], extra = 0, can_delete = False)


class AnswerForm(ModelForm):
    """
    Форма для ответов
    """

    class Meta:
        model = Answer
        fields = '__all__'
