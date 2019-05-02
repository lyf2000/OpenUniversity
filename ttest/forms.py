from django import forms

class TestForm(forms.Form):
    questions = forms.ChoiceField(help_text='Выберите правильный ответ')