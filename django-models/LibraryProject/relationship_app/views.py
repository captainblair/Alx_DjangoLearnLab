# django_models/relationship/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile

def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship/member_view.html')
