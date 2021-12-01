from ninja import ModelSchema, Schema
from .models import Book

class BookSchema(ModelSchema):
    class Config:
        model = Book
        model_fields = ['id', 'title', 'author', 'cover']

class BookFav(Schema):
    id : int
    fav : bool

class BookDetailSchema(ModelSchema):
    liked : int
    disliked : int
    class Config:
        model = Book
        model_fields = ['id', 'title','author', 'summary', 'cover']