from datetime import datetime

from jose import jwt
from ninja.security import HttpBearer
from ninja.errors import HttpError
from czytelnia.settings import SECRET_KEY

from .models import User

key = SECRET_KEY

def create_JWT(**data):
    data['iat'] = datetime.now()
    token = jwt.encode(data, key, algorithm='HS256')
    return token

class JWT(HttpBearer):
    def authenticate(self, request, token):
        print(token)
        try:
            data = jwt.decode(token, key)
            if (datetime.fromtimestamp(data['iat']) - datetime.now()).days > 1:
                raise HttpError(401, 'Token has expired')
            return data
        except:
            raise HttpError(401, 'Token is invalid')