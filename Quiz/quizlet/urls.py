from django.urls import path
from .views import QuizListView, CategoryListView, ShowQuiz
from .models import Quiz

urlpatterns = [
    path('quizzes', QuizListView.as_view(), name="quiz_list"),
    path('quizzes/<int:pk>/', CategoryListView.as_view(), name="category_list"),
    path('category/<int:pk>/', ShowQuiz.as_view(), name='question_list')
    #path('category<int:Category_id>/questions')
]