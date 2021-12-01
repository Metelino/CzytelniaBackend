from typing import List

from ninja import Router
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.http import FileResponse

from user.jwt import JWT
from user.models import User
from .models import Book
from .schemas import BookSchema, BookDetailSchema, BookFav


api = Router()

@api.get("{book_id}", response={200 : BookDetailSchema})
def book_detail(request, id : int):
    book = get_object_or_404(Book, id=id)
    return 200, book

@api.get("", response={200 : List[BookSchema]})
def book_list(request, book_name : str = None, page_num : int = 1):
    books = None
    if book_name is None:
        books = Book.objects.all()
    else:
        books = Book.objects.filter(name__icontains=book_name)

    p = Paginator(books, 10)
    books_page = p.get_page(page_num)

    return 200, list(books_page)

@api.get("{book_id}/cover")
def book_cover(request, book_id : int):
    book = get_object_or_404(Book, id=book_id)
    return FileResponse(open(book.cover.path, 'rb'), status=200)

@api.get("{book_id}/pdf", auth=JWT())
def book_page(request, book_id : int, page_num : int = 1):
    book = get_object_or_404(Book, id=book_id)
    #page_num = request.GET.get('page_num', 1)
    print(f'PATH : {book.content.path}')
    return FileResponse(open(book.content.path, 'rb'), status=200)