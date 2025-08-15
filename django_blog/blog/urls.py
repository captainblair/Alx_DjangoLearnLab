from django.urls import path
from . import views

urlpatterns = [
    # existing post URLs...
    path('search/', views.search_posts, name='search-posts'),
    path('tags/<str:tag_name>/', views.posts_by_tag, name='posts-by-tag'),
]
