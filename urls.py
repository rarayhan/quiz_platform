from django.urls import path
from . import views

app_name = 'quiz'

urlpatterns = [
    path('create/', views.create_quiz, name='create_quiz'),
    path('list/', views.quiz_list, name='quiz_list'),
    path('take/<int:quiz_id>/', views.take_quiz, name='take_quiz'),
    path('result/<int:quiz_id>/', views.quiz_result, name='quiz_result'),
    path('leaderboard/<int:quiz_id>/', views.leaderboard, name='leaderboard'),
]
