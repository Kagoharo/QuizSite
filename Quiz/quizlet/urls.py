from django.urls import path
from .views import CategoryListView, QuizDetailView, CategoryDetailView
from .crud_methods import category_create_view, category_update_view, quiz_create_view, quiz_update_view

urlpatterns = [
    path('quizzes/', CategoryListView.as_view(), name="category_list"),
    path('quizzes/post/', category_create_view, name="category_create"),
    path('quizzes/update/<int:pk>/', category_update_view, name="category_update"),
    path('quizzes/category/<int:pk>/', CategoryDetailView.as_view(), name='quiz_list'),
    path('quizzes/category/<int:pk>/post/', quiz_create_view, name="quiz_create"),
    path('quizzes/category/<int:pk>/update/', quiz_update_view, name="quiz_update"),
    path('quizzes/quiz/<int:pk>/', QuizDetailView.as_view(), name='questions')
]
