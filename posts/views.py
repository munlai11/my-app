from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Comment, Role, Industry, Company
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q, Count


def home(request):
    posts = Post.objects.all()
    banking_posts = Post.objects.filter(industry__name__contains='Banking').order_by('-created_date')[:5]
    consulting_posts = Post.objects.filter(industry__name__contains='Consulting').order_by('-created_date')[:5]
    engineering_posts = Post.objects.filter(industry__name__contains='Engineering').order_by('-created_date')[:5]
    law_posts = Post.objects.filter(industry__name__contains='Law').order_by('-created_date')[:5]
    healthcare_posts = Post.objects.filter(industry__name__contains='Healthcare').order_by('-created_date')[:5]
    sport_posts = Post.objects.filter(industry__name__contains='Sport').order_by('-created_date')[:5]
    government_posts = Post.objects.filter(industry__name__contains='Government').order_by('-created_date')[:5]

    context = {'posts': posts,
               'banking_posts':banking_posts,
               'consulting_posts':consulting_posts,
               'engineering_posts':engineering_posts}

    return render(request, 'posts/post_list.html', context)

def post_detail(request, pk, slug):
    post = get_object_or_404(Post, pk=pk)
    posts = Post.objects.all()

    comments_all = Comment.objects.filter(post = post).order_by('created_date')

    paginator = Paginator(comments_all,1)
    
    page = request.GET.get('page')
    
    comments = paginator.get_page(page)

    context = {'post':post,
               'posts':posts,
               'comments':comments}

    return render(request, 'posts/single_post.html', context)

@login_required
def post_new(request):
    posts = Post.objects.all()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk,slug=post.slug)
    else:
        form = PostForm()
    context = {'form':form,
              'posts':posts}
    return render(request, 'posts/post_edit.html', context)

@login_required
def post_edit(request, pk, slug):
    post = get_object_or_404(Post, pk=pk)
    posts = Post.objects.all()
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk,slug=post.slug)
    else:
        form = PostForm(instance=post)
    context = {'form':form,
              'posts':posts}
    return render(request, 'posts/post_edit.html', context)

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'posts/index.html', {'posts': posts})

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

@login_required
def post_remove(request, pk, slug):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('home')

@login_required
def add_comment_to_post(request, pk, slug):
    post = get_object_or_404(Post, pk=pk)
    posts = Post.objects.all()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk, slug=post.slug)
    else:
        form = CommentForm()
    context = {'form':form,
              'posts':posts}
    return render(request, 'posts/add_comment_to_post.html', context)

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk, slug):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk, slug=comment.post.slug)

def category_list(request):
    roles = Role.objects.all()
    companies = Company.objects.all()
    industries = Industry.objects.all()
    context = {'roles':roles,'companies':companies,'industries':industries}
    
    return render(request, 'posts/category_list.html',context)

def role_detail(request,pk,slug):
    posts = Post.objects.all()
    role = get_object_or_404(Role,pk=pk)
    posts_latest = Post.objects.filter(role = role).order_by('-created_date')
    posts_popular = Post.objects.filter(role = role).order_by('comments')
    #posts_popular = Post.objects.annotate(number_of_comments=Count('comments', filter=Q(role=role)))
    
    context = {'posts':posts,
                'posts_latest':posts_latest,
               'posts_popular':posts_popular}
    
    return render(request,'posts/category_detail.html',context)

def company_detail(request,pk,slug):
    posts = Post.objects.all()
    company = get_object_or_404(Company,pk=pk)
    posts_latest = Post.objects.filter(company = company).order_by('-created_date')
    posts_popular = Post.objects.filter(company = company).order_by('comments')
    #posts_popular = Post.objects.annotate(number_of_comments=Count('comments', filter=Q(role=role)))
    
    context = {'posts':posts,
               'posts_latest':posts_latest,
               'posts_popular':posts_popular}
    
    return render(request,'posts/category_detail.html',context)

