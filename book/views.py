from django.http import FileResponse
from .models import Book

def book_cover(request, book_id):
    book = Book.objects.get(id=book_id)
    return FileResponse(open(book.cover.path, 'rb'))

def book_page(request, book_id):
    book = Book.objects.get(id=book_id)
    #page_num = request.GET.get('page_num', 0)
    print(f'PATH : {book.content.path}')
    return FileResponse(open(book.content.path, 'rb'))