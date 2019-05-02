from django import forms
from .models import Answer

class TestForm(forms.Form):
    questions = ''
    field = forms.ChoiceField(label="Question1", required=True,
                                  choices={(12, 'yse')}, widget=forms.RadioSelect)
    def __init__(self, questions):
        self.questions = questions
        # for question in questions:
        #     for answer in Answer.objects.filter(question=question):
        #         self.choises.append((answer.pk, answer.answer_text))

        # field = forms.ChoiceField(label=question.question_text, required=True,
        #                               choices=self.choises, widget=forms.RadioSelect)
    for question in questions:
        choises = []
        for answer in Answer.objects.filter(question=question):
            choises.append((answer.pk, answer.answer_text))
        field = forms.ChoiceField(label=question.question_text, required=True,
                                      choices=choises, widget=forms.RadioSelect)