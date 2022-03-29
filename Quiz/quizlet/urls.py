from django.urls import path
from .views import CategoryListView, QuestionListView, QuizListView

urlpatterns = [
    path('quizzes', CategoryListView.as_view(), name="category_list"),
    path('quizzes/<int:pk>/', QuizListView.as_view(), name="quiz_list"),
    path('category/<int:pk>/', QuestionListView.as_view(), name='question_list')
]