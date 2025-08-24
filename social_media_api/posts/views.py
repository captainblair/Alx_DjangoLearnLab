from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Post

class FeedView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        followed_users = request.user.following.all()
        posts = Post.objects.filter(author__in=followed_users).order_by("-created_at")
        data = [{"id": p.id, "content": p.content, "author": p.author.username} for p in posts]
        return Response({"feed": data})
