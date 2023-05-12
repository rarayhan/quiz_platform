from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import QuizForm, TakeQuizForm
from .models import Quiz, Score

@login_required
def take_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    
    if request.method == 'POST':
        form = TakeQuizForm(request.POST)
        if form.is_valid():
            score = 0
            for question in quiz.question_set.all():
                selected_choice = form.cleaned_data.get(f'question_{question.id}')
                if selected_choice == question.correct_choice:
                    score += 1
            Score.objects.create(user=request.user, quiz=quiz, score=score)
            return redirect('quiz:quiz_result', quiz_id=quiz_id)
    else:
        form = TakeQuizForm(quiz=quiz)
    
    return render(request, 'quiz/take_quiz.html', {'quiz': quiz, 'form': form})

@login_required
def quiz_result(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    score = Score.objects.filter(user=request.user, quiz=quiz).first()
    
    return render(request, 'quiz/quiz_result.html', {'quiz': quiz, 'score': score})

@login_required
def leaderboard(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    scores = Score.objects.filter(quiz=quiz).order_by('-score')
    
    return render(request, 'quiz/leaderboard.html', {'quiz': quiz, 'scores': scores})
