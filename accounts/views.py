from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from categories.models import Industry, Role, Company
from posts.models import Post, Comment
from interviews.models import Interview
from questions.models import Question, QuestionPart, get_random_question
from .models import Profile
from .forms import EditProfileForm, SignUpForm, EditDetailsForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q, Count
import datetime
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def signup(request):
    posts_home = Post.objects.all().order_by('-created_date')[:5]
    today_pick = get_random_question()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            user.profile.skype = form.cleaned_data.get('skype')
            user.save()
            return redirect('home')
    else:
        form = SignUpForm()

    context = {'form':form,
     'posts_home':posts_home,
     'today_pick':today_pick}

    return render(request, 'accounts/signup.html', context)

@login_required
def view_profile(request, pk, username):
    user_profile = get_object_or_404(User, pk=pk)
    posts_home = Post.objects.all().order_by('-created_date')[:5]
    today_pick = get_random_question()
    interviews_all = Interview.objects.filter(Q(author = request.user) | Q(partner = request.user)).order_by('interview_date')
    posts_all = Post.objects.filter(author = request.user).order_by('created_date')
    comments_all = Comment.objects.filter(author = request.user).order_by('created_date')
    questions_all = Question.objects.filter(author = request.user).order_by('created_date')

    context = {'user_profile':user_profile,
               'interviews_all':interviews_all,
               'posts_all':posts_all,
               'comments_all':comments_all,
               'questions_all':questions_all,
               'posts_home':posts_home,
               'today_pick':today_pick,}

    return render(request, 'accounts/single_profile.html', context)

@login_required
def edit_profile(request,pk,username):
    posts_home = Post.objects.all().order_by('-created_date')[:5]
    today_pick = get_random_question()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()

            return redirect('view_profile',pk=pk,username=username)
    else:
        form = EditProfileForm(instance=request.user)

    context = {'form':form,
               'posts_home':posts_home,
               'today_pick':today_pick}

    return render(request,'accounts/profile_edit.html',context)

def edit_details(request,pk,username):
    posts_home = Post.objects.all().order_by('-created_date')[:5]
    today_pick = get_random_question()
    if request.method == 'POST':
        #form = EditDetailsForm(request.POST, request.FILES, instance=request.user)
        form = EditDetailsForm(request.POST, request.FILES, instance=request.user.profile)

        if form.is_valid():
            user = form.save()

            #user.profile.dob = form.cleaned_data.get('dob')
            #user.profile.bio = form.cleaned_data.get('bio')
            #user.profile.skype = form.cleaned_data.get('skype')
            #user.profile.pic = request.FILES['pic']
            #user.profile.save()
            user.save()

            return redirect('view_profile',pk=pk,username=username)
    else:
        form = EditDetailsForm(instance=request.user.profile)

    context = {'form':form,
               'posts_home':posts_home,
               'today_pick':today_pick}

    return render(request,'accounts/details_edit.html',context)

