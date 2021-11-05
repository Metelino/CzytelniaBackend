from typing import List

from ninja import Router
from user.jwt import JWT
from django.core.paginator import Paginator

from user.models import User
from .models import Book
from .schemas import BookSchema, BookDetailSchema


api = Router()

@api.get("get/{id}", response=BookDetailSchema)
def book_detail(request, id : int):
    book = Book.objects.get(id=id)
    return book

@api.get("get", response=List[BookSchema])
def book_list(request, book_name : str = None, page_num : int = 1):
    books = None
    if book_name is None:
        books = Book.objects.all()
    else:
        books = Book.objects.filter(name__icontains=book_name)

    p = Paginator(books, 10)
    books_page = p.get_page(page_num)

    return list(books_page)

@api.get("get_favorite", response=List[BookSchema], auth=JWT())
def favorite_books(request):
    id = int(request.auth['sub'])
    profile = User.objects.get(id=id).profile
    return list(profile.books.all())

@api.get("add_favorite", response=List[BookSchema], auth=JWT())
def add_to_favorite(request):
    id = int(request.auth['sub'])
    profile = User.objects.get(id=id).profile
    return list(profile.books.all())