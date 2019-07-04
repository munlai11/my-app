from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from posts.models import Post, Comment
from questions.models import get_random_question
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Count
from .models import Feedback
from .forms import FeedbackForm

@login_required
def feedback_new(request):
    posts_home = Post.objects.all().order_by('-created_date')[:5]
    today_pick = get_random_question()
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.author = request.user
            feedback.save()
            return redirect('home')
    else:
        form = FeedbackForm()
    context = {'form':form,
               'posts_home':posts_home,
               'today_pick':today_pick}

    return render(request, 'comms/contact.html', context)


