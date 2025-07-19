from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# Helper functions to check user role
def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'

# View for Admin
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')

# View for Librarian
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')

# View for Member
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member_view.html')
