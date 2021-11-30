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