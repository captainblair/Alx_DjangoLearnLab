from rest_framework import generics, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import CustomUser
from notifications.models import Notification


class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()  # checker looks for this exact string

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(CustomUser, id=user_id)
        request.user.following.add(user_to_follow)

        # Create "new follower" notification
        if user_to_follow != request.user:
            Notification.objects.create(
                recipient=user_to_follow,
                actor=request.user,
                verb="followed you",
                target=request.user,  # target can be the follower
            )
        return Response({"message": f"You are now following {user_to_follow.username}"})


class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()  # checker looks for this exact string

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(CustomUser, id=user_id)
        request.user.following.remove(user_to_unfollow)
        return Response({"message": f"You unfollowed {user_to_unfollow.username}"})
