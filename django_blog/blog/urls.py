from django.urls import path
from .views import PostByTagListView

urlpatterns = [
    # your other paths...
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts-by-tag'),  # ✅
]
