from django.urls import path
from .views import CategoryListView, QuizDetailView, CategoryDetailView
from .crud_methods import category_create, category_update, quiz_create, quiz_update

urlpatterns = [
    path('quizzes/', CategoryListView.as_view(), name="category_list"),
    path('quizzes/post/', category_create, name="category_create"),
    path('quizzes/update/<int:pk>/', category_update, name="category_update"),
    path('quizzes/category/<int:pk>/', CategoryDetailView.as_view(), name='quiz_list'),
    path('quizzes/category/<int:pk>/post/', quiz_create, name="quiz_create"),
    path('quizzes/category/<int:pk>/update/', quiz_update, name="quiz_update"),
    path('quizzes/quiz/<int:pk>/', QuizDetailView.as_view(), name='questions')
]
