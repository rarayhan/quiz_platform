from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import QuizForm

@login_required
def create_quiz(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.creator = request.user
            quiz.save()
            return redirect('quiz:quiz_list')
    else:
        form = QuizForm()
    return render(request, 'quiz/create_quiz.html', {'form': form})

@login_required
def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz/quiz_list.html', {'quizzes': quizzes})

# Other views for quiz taking, scoring, and leaderboard
