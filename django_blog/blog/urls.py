# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # ... your existing post URLs
    path('tags/<str:tag_name>/', views.posts_by_tag, name='posts-by-tag'),  # ✅ tag filter
    path('search/', views.search_posts, name='search-posts'),  # ✅ search
]
