from django.urls import path
from . import views

app_name = 'quiz'

urlpatterns = [
    path('create/', views.create_quiz, name='create_quiz'),
    path('list/', views.quiz_list, name='quiz_list'),
    # Add URLs for quiz taking, scoring, and leaderboard
]
