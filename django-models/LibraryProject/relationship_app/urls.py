# django_models/relationship/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('admin-only/', views.admin_view, name='admin_view'),
    path('librarian-only/', views.librarian_view, name='librarian_view'),
    path('member-only/', views.member_view, name='member_view'),
]
