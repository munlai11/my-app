from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from posts.models import Post
from .models import Question, QuestionPart, get_random_question
from categories.models import Company, Industry, Role, Difficulty
from .forms import QuestionForm, QuestionPartForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Count

@login_required
def question_new(request):
    questions = Question.objects.all()
    posts_home = Post.objects.all().order_by('-created_date')[:5]
    today_pick = get_random_question()
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.published_date = timezone.now()
            question.save()
            return redirect('question_part_new', pk=question.pk,slug=question.slug)
    else:
        form = QuestionForm()
    context = {'form':form,
              'questions':questions,
              'posts_home':posts_home,
              'today_pick':today_pick}

    return render(request, 'questions/question_edit.html', context)

@login_required
def question_part_new(request,pk,slug):
    question = get_object_or_404(Question, pk=pk)
    questions = Question.objects.all()
    posts_home = Post.objects.all().order_by('-created_date')[:5]
    today_pick = get_random_question()
    if request.method == "POST":
        form = QuestionPartForm(request.POST)
        if form.is_valid():
            question_part = form.save(commit=False)
            question_part.question = question
            question_part.author = request.user
            question_part.question_number = QuestionPart.objects.filter(question=question).count() + 1
            question_part.save()
            return redirect('question_detail', pk=question.pk, slug=question.slug)
    else:
        form = QuestionPartForm()
    context = {'form':form,
               'questions':questions,
               'posts_home':posts_home,
               'today_pick':today_pick}

    return render(request, 'questions/question_part_edit.html', context)

def question_detail(request, pk, slug):
    question = get_object_or_404(Question, pk=pk)
    questions = Question.objects.all()
    posts_home = Post.objects.all().order_by('-created_date')[:5]
    today_pick = get_random_question()
    parts_all = QuestionPart.objects.filter(question = question).order_by('created_date')

    context = {'question':question,
               'questions':questions,
               'posts_home':posts_home,
               'today_pick':today_pick}

    return render(request, 'questions/single_question.html', context)

@login_required
def question_remove(request, pk, slug):
    question = get_object_or_404(Question, pk=pk)
    question.delete()
    return redirect('home')

def question_list(request):
    questions_all = Question.objects.all().order_by('-created_date')
    posts_home = Post.objects.all().order_by('-created_date')[:5]
    today_pick = get_random_question()
    banking_questions = Question.objects.filter(industry__name__contains='Banking').order_by('-created_date')
    consulting_questions = Question.objects.filter(industry__name__contains='Consulting').order_by('-created_date')
    technology_questions = Question.objects.filter(industry__name__contains='Technology').order_by('-created_date')
    law_questions  = Question.objects.filter(industry__name__contains='Law').order_by('-created_date')
    healthcare_questions  = Question.objects.filter(industry__name__contains='Healthcare').order_by('-created_date')
    sport_questions = Question.objects.filter(industry__name__contains='Sport').order_by('-created_date')
    government_questions  = Question.objects.filter(industry__name__contains='Government').order_by('-created_date')
    other_questions  = Question.objects.filter(industry__name__contains='Other').order_by('-created_date')

    context = {'questions_all':questions_all,
               'posts_home':posts_home,
               'today_pick':today_pick,
               'banking_questions':banking_questions,
               'consulting_questions':consulting_questions,
               'technology_questions':technology_questions,
               'law_questions':law_questions,
               'healthcare_questions':healthcare_questions,
               'sport_questions':sport_questions,
               'government_questions':government_questions,
               'other_questions':other_questions}

    return render(request, 'questions/question_list.html', context)

@login_required
def like_question(request, pk, slug):
    question = get_object_or_404(Question, pk=pk)

    if question.likes.filter(pk = request.user.pk).exists():
        question.likes.remove(request.user)
        question.save()

    else:
        question.likes.add(request.user)
        question.save()

    return redirect('question_detail',pk=question.pk, slug=question.slug)