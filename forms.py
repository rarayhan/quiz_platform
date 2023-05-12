from django import forms
from .models import Question

class TakeQuizForm(forms.Form):
    def __init__(self, *args, **kwargs):
        quiz = kwargs.pop('quiz')
        super().__init__(*args, **kwargs)
        for question in quiz.question_set.all():
            choices = [(choice.id, choice.choice_text) for choice in question.choice_set.all()]
            self.fields[f'question_{question.id}'] = forms.ChoiceField(
                label=question.question_text,
                widget=forms.RadioSelect,
                choices=choices,
                required=True,
            )
