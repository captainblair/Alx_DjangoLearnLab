from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post
from accounts.models import Follow

@login_required
def feed(request):
    # Get the list of users that the current user is following
    following_users = Follow.objects.filter(follower=request.user).values_list('following', flat=True)

    # Get posts authored by those users, ordered by most recent
    posts = Post.objects.filter(author__in=following_users).order_by('-created_at')

    return render(request, 'posts/feed.html', {'posts': posts})
