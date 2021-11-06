from django.shortcuts import get_object_or_404
from ninja import Router
from ninja.errors import HttpError

from .models import User
from .schemas import UserIn, UserOut

from .jwt import create_JWT, JWT

api = Router()

@api.post('login')
def login(request, data : UserIn):
    user = get_object_or_404(User, username=data.username)
    if not user.password == data.password:
        raise HttpError(503, "Błędne hasło")
    print(f'{user.id}')
    return {'token' : create_JWT(sub = str(user.id), name = user.username)}
    #return user

@api.post('register', response=UserOut)
def register(request, data : UserIn):
    user = User.objects.create(username=data.username, password=data.password)
    return {'token' : create_JWT(sub = str(user.id), name = user.username)}