from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Interview
from .forms import InterviewForm
from posts.models import Post, Comment
from questions.models import get_random_question
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Count
import datetime

@login_required
def interview_new(request):
    posts_home = Post.objects.all().order_by('-created_date')[:5]
    today_pick = get_random_question()
    interviews = Interview.objects.all()
    if request.method == "POST":
        form = InterviewForm(request.POST)
        if form.is_valid():
            interview = form.save(commit=False)
            interview.author = request.user
            interview.save()
            return redirect('interview_detail', pk=interview.pk,slug=interview.slug)
    else:
        form = InterviewForm()
    context = {'form':form,
              'interviews':interviews,
              'posts_home':posts_home,
              'today_pick':today_pick}

    return render(request, 'interviews/interview_edit.html', context)

def interview_detail(request, pk, slug):
    posts_home = Post.objects.all().order_by('-created_date')[:5]
    today_pick = get_random_question()
    interview = get_object_or_404(Interview, pk=pk)
    interviews = Interview.objects.all()

    context = {'interview':interview,
               'interviews':interviews,
               'posts_home':posts_home,
               'today_pick':today_pick}

    return render(request, 'interviews/single_interview.html', context)

def interview_accept(request, pk, slug):
    posts_home = Post.objects.all().order_by('-created_date')[:5]
    today_pick = get_random_question()
    interview = get_object_or_404(Interview, pk=pk)
    interview.partner = request.user
    interview.accept()
    context = {'interview':interview,
               'posts_home':posts_home,
               'today_pick':today_pick}

    return render(request, 'interviews/single_interview.html', context)

def interview_cancel(request, pk, slug):
    interview = get_object_or_404(Interview, pk=pk)
    if interview.partner == request.user:
        interview.cancel()
    elif interview.author == request.user:
        interview.delete()

    return redirect('interview_list')

def interview_list(request):
    day0 = datetime.date.today()
    day1 = day0 + datetime.timedelta(days=1)
    day2 = day1 + datetime.timedelta(days=1)
    day3 = day2 + datetime.timedelta(days=1)
    day4 = day3 + datetime.timedelta(days=1)
    day5 = day4 + datetime.timedelta(days=1)
    day6 = day5 + datetime.timedelta(days=1)
    
    posts = Post.objects.all()
    posts_home = Post.objects.all().order_by('-created_date')[:5]
    today_pick = get_random_question()
    interview_day0 = Interview.objects.filter(interview_date__contains = day0).filter(accepted = False).order_by('interview_time')
    interview_day1 = Interview.objects.filter(interview_date__contains = day1).filter(accepted = False).order_by('interview_time')
    interview_day2 = Interview.objects.filter(interview_date__contains = day2).filter(accepted = False).order_by('interview_time')
    interview_day3 = Interview.objects.filter(interview_date__contains = day3).filter(accepted = False).order_by('interview_time')
    interview_day4 = Interview.objects.filter(interview_date__contains = day4).filter(accepted = False).order_by('interview_time')
    interview_day5 = Interview.objects.filter(interview_date__contains = day5).filter(accepted = False).order_by('interview_time')
    interview_day6 = Interview.objects.filter(interview_date__contains = day6).filter(accepted = False).order_by('interview_time')

    context = {'posts':posts,
               'posts_home':posts_home,
               'today_pick':today_pick,
               'day2':day2,
               'day3':day3,
               'day4':day4,
               'day5':day5,
               'day6':day6,
               'interview_day0':interview_day0,
               'interview_day1':interview_day1,
               'interview_day2':interview_day2,
               'interview_day3':interview_day3,
               'interview_day4':interview_day4,
               'interview_day5':interview_day5,
               'interview_day6':interview_day6}

    return render(request, 'interviews/interview_list.html', context)
