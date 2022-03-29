from django.urls import path
from .views import CategoryListView, QuestionDetailView, QuizDetailView

urlpatterns = [
    path('quizzes', CategoryListView.as_view(), name="category_list"),
    path('quizzes/<int:pk>/', QuizDetailView.as_view(), name="quiz_list"),
    path('category/<int:pk>/', QuestionDetailView.as_view(), name='question_list')
]