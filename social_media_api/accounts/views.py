from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

@login_required
def follow_user(request, username):
    user_to_follow = get_object_or_404(User, username=username)
    if request.user == user_to_follow:
        return HttpResponseForbidden("You cannot follow yourself.")
    request.user.profile.following.add(user_to_follow.profile)
    return redirect('profile', username=username)

@login_required
def unfollow_user(request, username):
    user_to_unfollow = get_object_or_404(User, username=username)
    if request.user == user_to_unfollow:
        return HttpResponseForbidden("You cannot unfollow yourself.")
    request.user.profile.following.remove(user_to_unfollow.profile)
    return redirect('profile', username=username)
