from django.shortcuts import render, redirect
from .models import Follow
from userProfile.models import Profile


def following(request):
    if request.method == 'POST':
        request_id = request.POST["following_id"]
        follow_rq = Follow.objects.filter(pk=request_id).update(approved=True)
        return redirect('home')

    userprofile = Profile.objects.get(user=request.user)

    following = Follow.objects.filter(
        user_profile=userprofile, approved=False).all()

    following_request = Follow.objects.filter(
        follow_profile=userprofile, approved=False).all()

    data = {
        'following': following,
        'following_request': following_request,
        'userprofile': userprofile,
    }
    return render(request, 'follow/following.html', data)


def followers(request):
    userprofile = Profile.objects.get(user=request.user)
    followers = Follow.objects.filter(
        user_profile=userprofile, approved=True).all()
    accepted_request = Follow.objects.filter(
        follow_profile=userprofile, approved=True).all()
    data = {
        'followers': followers,
        'userprofile': userprofile,
        'accepted_requests': accepted_request,
    }

    return render(request, 'follow/followers.html', data)


def individual_following(request, id):
    print("ID:>>>>:", id)
    userprofile = Profile.objects.get(id=id)
    profile = Profile.objects.filter(id=id)
    following = Follow.objects.filter(
        user_profile=userprofile, approved=False)
    following_request = Follow.objects.filter(
        follow_profile=userprofile, approved=False).all()
    # print(following)
    data = {
        'following': following,
        'following_request': following_request,
        'userprofile': userprofile,
    }
    return render(request, 'follow/individual_following.html', data)


def individual_followers(request, id):
    print("ID:>>>>:", id)
    userprofile = Profile.objects.get(id=id)
    profile = Profile.objects.filter(id=id)
    followers = Follow.objects.filter(
        user_profile=userprofile, approved=True)
    followers_request = Follow.objects.filter(
        follow_profile=userprofile, approved=True).all()
    # print(following)
    data = {
        'followers': followers,
        'followers_request': followers_request,
        'userprofile': userprofile,
    }
    return render(request, 'follow/individual_followers.html', data)
