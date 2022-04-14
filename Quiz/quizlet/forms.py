from django.forms import ModelForm, inlineformset_factory, BaseInlineFormSet
from .models import Category, Quiz, Answer, Question, UserAnswers


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


class AnswerForm(ModelForm):
    """
    Форма для ответов
    """

    class Meta:
        model = Answer
        fields = '__all__'


class UserAnswersForm(ModelForm):
    """
    Форма для ответов пользователя
    """

    class Meta:
        model = UserAnswers
        fields = '__all__'


class CustomUserAnswerInlineFormSet(BaseInlineFormSet):
    pass


UserAnswerFormSet = inlineformset_factory(
    Answer, UserAnswers, form = UserAnswersForm, formset = CustomUserAnswerInlineFormSet,
    fields = ['user', 'answer'], extra = 0, can_delete = False)
