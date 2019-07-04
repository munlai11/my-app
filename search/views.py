from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from categories.models import Industry, Role, Company
from posts.models import Post, Comment
from interviews.models import Interview
from questions.models import Question, QuestionPart, get_random_question
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q, Count
import datetime


def category_list(request):
    posts_home = Post.objects.all().order_by('-created_date')[:5]
    today_pick = get_random_question()
    roles = Role.objects.all()
    companies = Company.objects.all()
    industries = Industry.objects.all()
    context = {'posts_home':posts_home,
               'today_pick':today_pick,
               'roles':roles,
               'companies':companies,
               'industries':industries}
    
    return render(request, 'search/category_list.html',context)

def industry_detail(request, pk, slug):
    today = datetime.date.today()
    posts= Post.objects.all()
    posts_home = Post.objects.all().order_by('-created_date')[:5]
    today_pick = get_random_question()
    industry = get_object_or_404(Industry, pk=pk)
    posts_latest = Post.objects.filter(industry = industry).order_by('-created_date')
    posts_popular = Post.objects.filter(industry = industry).order_by('likes', 'comments')
    questions_latest = Question.objects.filter(industry = industry).order_by('-created_date')
    questions_popular = Question.objects.filter(industry = industry).order_by('likes')
    interview_latest = Interview.objects.filter(industry = industry, interview_date__gte = today).order_by('interview_date','interview_time')

        
    context = {'posts':posts,
               'posts_home':posts_home,
               'today_pick':today_pick,
               'industry':industry,
                'posts_latest':posts_latest,
               'posts_popular':posts_popular,
               'questions_latest':questions_latest,
               'questions_popular':questions_popular,
               'interview_latest':interview_latest}

    return render(request,'search/category_detail.html',context)

def role_detail(request,pk,slug):
    today = datetime.date.today()
    posts = Post.objects.all()
    posts_home = Post.objects.all().order_by('-created_date')[:5]
    today_pick = get_random_question()
    role = get_object_or_404(Role,pk=pk)
    posts_latest = Post.objects.filter(role = role).order_by('-created_date')
    posts_popular = Post.objects.filter(role = role).order_by('likes','comments')
    questions_latest = Question.objects.filter(role = role).order_by('-created_date')
    questions_popular = Question.objects.filter(role = role).order_by('likes')
    interview_latest = Interview.objects.filter(role = role, interview_date__gte = today).order_by('interview_date','interview_time')
    #posts_popular = Post.objects.annotate(number_of_comments=Count('comments', filter=Q(role=role)))
    
    context = {'posts':posts,
               'posts_home':posts_home,
               'today_pick':today_pick,
               'role':role,
                'posts_latest':posts_latest,
               'posts_popular':posts_popular,
               'questions_latest':questions_latest,
               'questions_popular':questions_popular,
               'interview_latest':interview_latest}
    
    return render(request,'search/category_detail.html',context)

def company_detail(request,pk,slug):
    today = datetime.date.today()
    posts = Post.objects.all()
    posts_home = Post.objects.all().order_by('-created_date')[:5]
    today_pick = get_random_question()
    company = get_object_or_404(Company,pk=pk)
    posts_latest = Post.objects.filter(company = company).order_by('-created_date')
    posts_popular = Post.objects.filter(company = company).order_by('likes','comments')
    questions_latest = Question.objects.filter(company = company).order_by('-created_date')
    questions_popular = Question.objects.filter(company = company).order_by('likes')
    interview_latest = Interview.objects.filter(company = company, interview_date__gte = today).order_by('interview_date','interview_time')
    #posts_popular = Post.objects.annotate(number_of_comments=Count('comments', filter=Q(role=role)))
    
    context = {'posts':posts,
               'posts_home':posts_home,
               'today_pick':today_pick,
               'company':company,
                'posts_latest':posts_latest,
               'posts_popular':posts_popular,
               'questions_latest':questions_latest,
               'questions_popular':questions_popular,
               'interview_latest':interview_latest}
    
    return render(request,'search/category_detail.html',context)


