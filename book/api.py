from typing import List

from ninja import Router
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.http import FileResponse

from user.jwt import JWT
from user.models import User
from .models import Book
from .schemas import BookSchema, BookDetailSchema


api = Router()

@api.get("get/{id}", response={200 : BookDetailSchema})
def book_detail(request, id : int):
    book = get_object_or_404(Book, id=id)
    return 200, book

@api.get("get", response={200 : List[BookSchema]})
def book_list(request, book_name : str = None, page_num : int = 1):
    books = None
    if book_name is None:
        books = Book.objects.all()
    else:
        books = Book.objects.filter(name__icontains=book_name)

    p = Paginator(books, 10)
    books_page = p.get_page(page_num)

    return 200, list(books_page)

@api.get("get_favorite", response={200 : List[BookSchema]}, auth=JWT())
def favorite_books(request):
    id = int(request.auth['sub'])
    profile = User.objects.get(id=id).profile
    return 200, list(profile.books.all())

@api.get("check_favorite", response={200 : bool}, auth=JWT())
def check_favorite(request, book_id):
    id = int(request.auth['sub'])
    profile = User.objects.get(id=id).profile
    if profile.books.filter(id=book_id).exists():
        return 200, True
    return 200, False


@api.get("add_favorite/{book_id}", response={204 : bool}, auth=JWT())
def add_to_favorite(request, book_id : int):
    id = int(request.auth['sub'])
    book = get_object_or_404(Book, id=book_id)
    profile = User.objects.get(id=id).profile
    if profile.books.filter(id=book.id).exists():
        profile.books.exclude(book)
    else:
        profile.books.add(book)
    return 204, None

@api.get("get_cover/{book_id}")
def book_cover(request, book_id : int):
    book = get_object_or_404(Book, id=book_id)
    return FileResponse(open(book.cover.path, 'rb'), status=200)

@api.get("get_page/{book_id}", auth=JWT())
def book_page(request, book_id : int, page_num : int = 1):
    book = get_object_or_404(Book, id=book_id)
    #page_num = request.GET.get('page_num', 1)
    print(f'PATH : {book.content.path}')
    return FileResponse(open(book.content.path, 'rb'), status=200)