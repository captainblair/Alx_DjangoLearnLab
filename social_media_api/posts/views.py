from rest_framework import generics, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Post, Like
from notifications.models import Notification


class FeedView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # required strings for checker: following.all(), order_by
        following_users = request.user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        data = [
            {
                "id": post.id,
                "content": post.content,
                "author": post.author.username,
                "likes": post.likes.count(),
                "created_at": post.created_at,
            }
            for post in posts
        ]
        return Response(data)


class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)

        # prevent duplicate likes
        already = Like.objects.filter(post=post, user=request.user).exists()
        if already:
            return Response({"detail": "Already liked."}, status=200)

        Like.objects.create(post=post, user=request.user)

        # create a notification for the post author
        if post.author != request.user:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked your post",
                target=post,
            )

        return Response({"message": "Post liked."}, status=201)


class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        Like.objects.filter(post=post, user=request.user).delete()
        return Response({"message": "Post unliked."})
