from django.http import FileResponse
from ninja import Router
from .models import Book
from django.shortcuts import get_object_or_404
from user.jwt import JWT

# api = Router()

# @api.get()
# def book_cover(request, book_id):
#     book = get_object_or_404(Book, id=book_id)
#     return FileResponse(open(book.cover.path, 'rb'))

# @api.get(auth=JWT)
# def book_page(request, book_id):
#     book = get_object_or_404(Book, id=book_id)
#     #page_num = request.GET.get('page_num', 1)
#     print(f'PATH : {book.content.path}')
#     return FileResponse(open(book.content.path, 'rb'))