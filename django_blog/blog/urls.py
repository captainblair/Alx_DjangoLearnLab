from django.urls import path
from . import views

urlpatterns = [
    # existing post URLs...
    path('post/<int:pk>/comment/new/', views.add_comment, name='add-comment'),
    path('comment/<int:pk>/edit/', views.edit_comment, name='edit-comment'),
    path('comment/<int:pk>/delete/', views.delete_comment, name='delete-comment'),
]
