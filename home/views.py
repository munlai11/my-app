from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from posts.models import Post, Comment
from questions.models import Question, get_random_question
from django.contrib.auth.decorators import login_required

def home(request):
    posts_all = Post.objects.all().order_by('-created_date')
    posts_home = Post.objects.all().order_by('-created_date')[:5]
    today_pick = get_random_question()
    banking_posts = Post.objects.filter(industry__name__contains='Banking').order_by('-created_date')
    consulting_posts = Post.objects.filter(industry__name__contains='Consulting').order_by('-created_date')
    technology_posts = Post.objects.filter(industry__name__contains='Technology').order_by('-created_date')
    law_posts = Post.objects.filter(industry__name__contains='Law').order_by('-created_date')
    healthcare_posts = Post.objects.filter(industry__name__contains='Healthcare').order_by('-created_date')
    sport_posts = Post.objects.filter(industry__name__contains='Sport').order_by('-created_date')
    government_posts = Post.objects.filter(industry__name__contains='Government').order_by('-created_date')
    other_posts = Post.objects.filter(industry__name__contains='Other').order_by('-created_date')

    context = {'posts_all':posts_all,
               'posts_home':posts_home,
               'today_pick':today_pick,
               'banking_posts':banking_posts,
               'consulting_posts':consulting_posts,
               'technology_posts':technology_posts,
               'law_posts':law_posts,
               'healthcare_posts':healthcare_posts,
               'sport_posts':sport_posts,
               'government_posts':government_posts,
               'other_posts':other_posts}

    return render(request, 'posts/post_list.html', context)
