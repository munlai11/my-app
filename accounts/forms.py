from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import SelectDateWidget, SplitDateTimeWidget, TimeInput

class SignUpForm(UserCreationForm):
    skype = forms.CharField(max_length=100, help_text='This will only be used for arranging practice interviews')
    
    class Meta:
        model = User
        fields = ('username', 'email','skype', 'password1', 
        'password2')

class EditProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
        ) 

class EditDetailsForm(forms.ModelForm):

    #pic = forms.ImageField( help_text="Profile Picture", required = False)    
    dob = forms.DateField(    widget = SelectDateWidget(
        empty_label=("Choose Year", "Choose Month", "Choose Day"),
    ),help_text="Date of Birth")
    #bio = forms.CharField(max_length=50,required = False,help_text="Short Bio")
    #skype = forms.CharField(max_length=100 help_text='This will only be used for arranging practice interviews')


    class Meta:
        model = Profile
        fields = (
            'skype',
            'pic',
            'dob',
            'bio',
        )

