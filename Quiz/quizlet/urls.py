from django.urls import path
from . import views
from .views import QuizListView, CategoryListView, ShowQuiz

urlpatterns = [
    path('quizzes', QuizListView.as_view(), name="quiz_list"),
    path('quizzes/<int:Quiz_pk>/', CategoryListView.as_view(), name="category_list"),
    path('category/<int:Quiz_pk>/', ShowQuiz.as_view(), name='question_list')
    #path('category<int:Category_id>/questions')
]