from django.urls import path
from .views import FollowUserView, UnfollowUserView, ListUsersView

urlpatterns = [
    path("follow/<int:user_id>/", FollowUserView.as_view(), name="follow_user"),
    path("unfollow/<int:user_id>/", UnfollowUserView.as_view(), name="unfollow_user"),
    path("users/", ListUsersView.as_view(), name="list_users"),
]
