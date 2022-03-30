from django.urls import path
from .views import CategoryListView, QuestionDetailView, CategoryDetailView

urlpatterns = [
    path('quizzes', CategoryListView.as_view(), name="category_list"),
    path('quizzes/category/<int:pk>/', CategoryDetailView.as_view(), name='category'),
    path('category/<int:pk>/', QuestionDetailView.as_view(), name='quiz')
]