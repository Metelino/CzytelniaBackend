from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router
from ninja.errors import HttpError

from .models import User
from .schemas import UserIn, UserOut, Token
from book.schemas import BookSchema, BookFav
from book.models import Book

from .jwt import create_JWT, JWT

api = Router()

@api.post('login', response={200 : Token})
def login(request, data : UserIn):
    user = get_object_or_404(User, username=data.username)
    if not user.password == data.password:
        raise HttpError(401, "Wrong password")
    return 200, {'id' : user.id, 'token' : create_JWT(sub = str(user.id), name = user.username)}
    #return user

@api.post('register', response={200 : Token})
def register(request, data : UserIn):
    user = None
    try:
        user = User.objects.create(username=data.username, password=data.password)
    except:
        raise HttpError(409, "Username already taken")
    return 200, {'id' : user.id, 'token' : create_JWT(sub = str(user.id), name = user.username)}

@api.get("favorite", response={200 : List[BookSchema]}, auth=JWT())
def favorite_books(request):
    id = int(request.auth['sub'])
    profile = User.objects.get(id=id).profile
    return 200, list(profile.books.all())

@api.get("favorite/{book_id}", response={200 : BookFav}, auth=JWT())
def check_favorite(request, book_id):
    id = int(request.auth['sub'])
    profile = User.objects.get(id=id).profile
    if profile.books.filter(id=book_id).exists():
        return 200, {'id' : book_id, 'fav' : True}
    return 200, {'id' : book_id, 'fav' : False}

@api.put("favorite/{book_id}", response={204 : None}, auth=JWT())
def add_to_favorite(request, book_id : int):
    id = int(request.auth['sub'])
    book = get_object_or_404(Book, id=book_id)
    profile = User.objects.get(id=id).profile
    if profile.books.filter(id=book.id).exists():
        profile.books.remove(book)
    else:
        profile.books.add(book)
    return 204, None