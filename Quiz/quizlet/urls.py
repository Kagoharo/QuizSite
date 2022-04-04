from django.urls import path
from .views import CategoryListView, QuizDetailView, CategoryDetailView, CategoryCreateView, CategoryUpdateView, QuizCreateView, QuizUpdateView

urlpatterns = [
    path('quizzes/', CategoryListView.as_view(), name="category_list"),
    path('quizzes/post/', CategoryCreateView.as_view(), name="category_create"),
    path('quizzes/update/<int:pk>/', CategoryUpdateView.as_view(), name="category_update"),
    path('quizzes/category/<int:pk>/', CategoryDetailView.as_view(), name='quiz_list'),
    path('quizzes/category/<int:pk>/post/', QuizCreateView.as_view(), name="quiz_create"),
    path('quizzes/category/<int:pk>/update/', QuizUpdateView.as_view(), name="quiz_update"),
    path('quizzes/quiz/<int:pk>/', QuizDetailView.as_view(), name='questions')
]
