from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse

@permission_required('bookshelf.can_create')
def create_book(request):
    return HttpResponse("Book created")

@permission_required('bookshelf.can_delete')
def delete_book(request):
    return HttpResponse("Book deleted")
