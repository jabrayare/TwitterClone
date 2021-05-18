from django.shortcuts import render, redirect
from .form import userProfileForm, userProfileUpdateForm
from .models import Profile
from django.db.models import Q
from follow.form import FollowForm
from follow.models import Follow
from django.contrib import messages


def create_profile(request):
    if request.method == 'POST':
        form = userProfileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(
                request, 'Your profile has been created successfully!')
            return redirect('home')
        else:
            return redirect('create_profile')
    else:
        form = userProfileForm()
    data = {
        "form": form
    }
    return render(request, 'userProfile/create_profile.html', data)


def editProfile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        profileForm = userProfileUpdateForm(
            request.POST, request.FILES, instance=profile)
        if profileForm.is_valid():
            profileForm.save()
            messages.success(
                request, 'Your profile has been updated successfully!')
            return redirect('userprofile')
    else:
        profileForm = userProfileUpdateForm()
    data = {
        'profile': profile,
        'profileForm': profileForm,
    }
    return render(request, 'userProfile/edit_profile.html', data)


def userProfile(request):
    if request.method == 'POST':
        user = request.POST["follow_user"]
        profile_user = Profile.objects.get(user=request.user)
        profile_follow = Profile.objects.get(first_name=user)
        if not Follow.objects.filter(user_profile=profile_user, follow_profile=profile_follow, approved=False).exists():
            follow = Follow.objects.create(
                user_profile=profile_user, follow_profile=profile_follow, approved=False)
            follow.save()
            return redirect('home')
        else:
            return redirect('userprofile')

    userprofile = Profile.objects.get(user=request.user)
    threeUsers = Profile.objects.filter(~Q(user=request.user)).all()

    following_values = list(Follow.objects.values_list('follow_profile_id', flat=True).filter(
        user_profile=userprofile).distinct())

    following_request_values = list(Follow.objects.values_list('user_profile_id', flat=True).filter(
        follow_profile=userprofile).distinct())

    follows = following_values + following_request_values

    following_count = Follow.objects.filter(
        user_profile=userprofile, approved=False).count()
    following_request_count = Follow.objects.filter(
        follow_profile=userprofile, approved=False).all().count()

    followers_request_count = Follow.objects.filter(
        follow_profile=userprofile, approved=True).all().count()
    followers_count = Follow.objects.filter(
        user_profile=userprofile, approved=True).count()

    data = {
        'userprofile': userprofile,
        'threeUsers': threeUsers,
        'following_count': following_count+following_request_count,
        'followers_count': followers_count + followers_request_count,
        'follows': follows,
    }
    return render(request, 'userProfile/userProfile.html', data)


def userProfile_accounts(request):
    accounts = Profile.objects.filter(~Q(user=request.user)).all()
    userprofile = Profile.objects.get(user=request.user)
    threeUsers = Profile.objects.filter(~Q(user=request.user)).all()

    following_values = list(Follow.objects.values_list('follow_profile_id', flat=True).filter(
        user_profile=userprofile).distinct())

    following_request_values = list(Follow.objects.values_list('user_profile_id', flat=True).filter(
        follow_profile=userprofile).distinct())

    follows = following_values + following_request_values
    data = {
        'accounts': accounts,
        'threeUsers': threeUsers,
        'follows': follows,
    }
    return render(request, 'userProfile/userProfile_accounts.html', data)


def individual_profile_page(request, id):
    userprofile = Profile.objects.get(pk=id)
    profile = Profile.objects.filter(pk=id)
    following_count = Follow.objects.filter(
        user_profile=userprofile, approved=False).count()
    following_request_count = Follow.objects.filter(
        follow_profile=userprofile, approved=False).all().count()

    followers_request_count = Follow.objects.filter(
        follow_profile=userprofile, approved=True).all().count()
    followers_count = Follow.objects.filter(
        user_profile=userprofile, approved=True).count()

    data = {
        'userprofile': userprofile,
        'following_count': following_count+following_request_count,
        'followers_count': followers_count + followers_request_count,
    }
    return render(request, 'userProfile/individualprofile.html', data)
