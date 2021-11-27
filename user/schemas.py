from ninja import ModelSchema, Schema
from .models import User

class Token(Schema):
    token : str

class UserIn(ModelSchema):
    class Config:
        model = User
        model_fields = ['username', 'password']

class UserOut(ModelSchema):
    class Config:
        model = User
        model_fields = ['id', 'username']