from ninja import ModelSchema
from .models import User

class UserIn(ModelSchema):
    class Config:
        model = User
        model_fields = ['username', 'password']

class UserOut(ModelSchema):
    class Config:
        model = User
        model_fields = ['id', 'username']