from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post

class FeedView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        following_users = request.user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        data = [{"id": post.id, "content": post.content, "author": post.author.username} for post in posts]
        return Response(data)
