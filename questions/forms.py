from django import forms
from .models import Question, QuestionPart

class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('title','difficulty', 'industry','role','company',)

class QuestionPartForm(forms.ModelForm):

    class Meta:
        model = QuestionPart
        fields = ( 'question_part','answer_part',)