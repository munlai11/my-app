from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def video(request):

    return render(request, 'video/index.html')

