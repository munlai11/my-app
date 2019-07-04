from django import forms
from .models import Interview
from django.forms.widgets import SelectDateWidget, SplitDateTimeWidget, TimeInput

class InterviewForm(forms.ModelForm):

    interview_date = forms.DateField(
    widget = SelectDateWidget(
        empty_label=("Choose Year", "Choose Month", "Choose Day"),
    ),)

    interview_time = forms.TimeField(widget = TimeInput( attrs={'placeholder': '14:00'})
    ,help_text='90 mins duration: Partner 1 = 45 mins | Partner 2 = 45 mins')

    class Meta:
        model = Interview
        fields = ('title','interview_date','interview_time', 'industry','role','company','difficulty', 'notes',)

