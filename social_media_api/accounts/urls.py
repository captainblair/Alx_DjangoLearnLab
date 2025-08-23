from django.urls import path
from .views import FollowUserView, UnfollowUserView, FollowingListView, FollowersListView

urlpatterns = [
    # existing auth routes...
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow'),
    path('following/', FollowingListView.as_view(), name='following-list'),
    path('followers/', FollowersListView.as_view(), name='followers-list'),
]
