from django.forms import ModelForm
from .models import Category, Quiz


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

