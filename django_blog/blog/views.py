# blog/views.py
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Post
from taggit.models import Tag

# ✅ search view
def search_posts(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct()
    return render(request, 'blog/search_results.html', {'results': results, 'query': query})

# ✅ posts by tag view
def posts_by_tag(request, tag_name):
    posts = Post.objects.filter(tags__name__in=[tag_name])
    return render(request, 'blog/tagged_posts.html', {'posts': posts, 'tag': tag_name})
