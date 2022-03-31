from django.urls import path
from .views import CategoryListView, QuizDetailView, CategoryDetailView

app_name = 'quizlet'

urlpatterns = [
    path('quizzes', CategoryListView.as_view(), name="category_list"),
    path('quizzes/category/<int:pk>/', CategoryDetailView.as_view(), name='category'),
    path('category/<int:pk>/', QuizDetailView.as_view(), name='quiz')
]