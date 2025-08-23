from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CustomUser

@login_required
def follow_user(request, user_id):
    # get the user to follow
    user_to_follow = get_object_or_404(CustomUser, id=user_id)
    # current user follows them
    request.user.following.add(user_to_follow)
    return redirect('feed')  # redirect to feed after following

@login_required
def unfollow_user(request, user_id):
    # get the user to unfollow
    user_to_unfollow = get_object_or_404(CustomUser, id=user_id)
    # remove from following
    request.user.following.remove(user_to_unfollow)
    return redirect('feed')

@login_required
def all_users(request):
    # required by test: "CustomUser.objects.all()"
    users = CustomUser.objects.all()
    return render(request, "accounts/all_users.html", {"users": users})
