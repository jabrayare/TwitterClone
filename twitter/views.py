from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from userProfile.models import Profile
from django.contrib.auth.models import User
from datetime import datetime


def landing_page(request):
    return render(request, 'twitterClone/landing_page.html')


@login_required
def home(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.authorprofile = Profile.objects.get(user=request.user)
            instance.save()
            return redirect('home')
    else:
        form = PostForm()

    posts = Post.objects.order_by('-created_date')
    userprofile = Profile.objects.get(user=request.user)

    data = {
        'posts': posts,
        'userprofile': userprofile,
        'datetime': datetime.now()
    }
    return render(request, 'twitterClone/main.html', data)
