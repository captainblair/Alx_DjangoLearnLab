from rest_framework import permissions, generics
from rest_framework.response import Response
from .models import Post

class FeedView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        following_users = request.user.following.all()  # 👈 ensures "following.all()" is present
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')  # 👈 order_by
        data = [
            {"id": post.id, "content": post.content, "author": post.author.username}
            for post in posts
        ]
        return Response(data)
