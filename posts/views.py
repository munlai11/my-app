from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Comment
from .forms import PostForm, CommentForm
from questions.models import get_random_question
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q, Count

def post_detail(request, pk, slug):
    post = get_object_or_404(Post, pk=pk)
    posts_home = Post.objects.all().order_by('-created_date')[:5]
    today_pick = get_random_question()
    comments_all = Comment.objects.filter(post = post).order_by('created_date')

    context = {'post':post,
               'posts_home':posts_home,
               'today_pick':today_pick}

    return render(request, 'posts/single_post.html', context)

@login_required
def post_new(request):
    posts_home = Post.objects.all().order_by('-created_date')[:5]
    today_pick = get_random_question()
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
              'posts_home':posts_home,
              'today_pick':today_pick}
    return render(request, 'posts/post_edit.html', context)

@login_required
def post_edit(request, pk, slug):
    post = get_object_or_404(Post, pk=pk)
    posts_home = Post.objects.all().order_by('-created_date')[:5]
    today_pick = get_random_question()
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
              'posts_home':posts_home,
              'today_pick':today_pick}
    return render(request, 'posts/post_edit.html', context)

@login_required
def post_remove(request, pk, slug):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('home')

@login_required
def add_comment_to_post(request, pk, slug):
    post = get_object_or_404(Post, pk=pk)
    posts_home = Post.objects.all().order_by('-created_date')[:5]
    today_pick = get_random_question()
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
              'posts_home':posts_home,
              'today_pick':today_pick}

    return render(request, 'posts/add_comment_to_post.html', context)

@login_required
def comment_remove(request, pk, slug):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk, slug=comment.post.slug)

@login_required
def like_post(request, pk, slug):
    post = get_object_or_404(Post, pk=pk)

    if post.likes.filter(pk = request.user.pk).exists():
        post.likes.remove(request.user)
        post.save()

    else:
        post.likes.add(request.user)
        post.save()

    return redirect('post_detail',pk=post.pk, slug=post.slug)

@login_required
def like_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post = get_object_or_404(Post, pk=comment.post.pk)
    
    if comment.likes.filter(pk = request.user.pk).exists():
        comment.likes.remove(request.user)
        post.save()
        comment.save()
        
    else:
        comment.likes.add(request.user)
        post.save()
        comment.save()

    return redirect('post_detail',pk=post.pk, slug=post.slug)

