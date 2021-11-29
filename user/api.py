from django.shortcuts import get_object_or_404
from ninja import Router
from ninja.errors import HttpError

from .models import User
from .schemas import UserIn, UserOut, Token

from .jwt import create_JWT, JWT

api = Router()

@api.post('login', response={200 : Token})
def login(request, data : UserIn):
    user = get_object_or_404(User, username=data.username)
    if not user.password == data.password:
        raise HttpError(503, "Wrong password")
    print(f'{user.id}')
    return 200, {'id' : user.id, 'token' : create_JWT(sub = str(user.id), name = user.username)}
    #return user

@api.post('register', response={200 : Token})
def register(request, data : UserIn):
    user = User.objects.create(username=data.username, password=data.password)
    return 200, {'id' : user.id, 'token' : create_JWT(sub = str(user.id), name = user.username)}