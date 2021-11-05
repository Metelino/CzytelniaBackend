from ninja import ModelSchema
from .models import Book

class BookSchema(ModelSchema):
    class Config:
        model = Book
        model_fields = ['name', 'author', 'cover']

class BookDetailSchema(ModelSchema):
    class Config:
        model = Book
        model_fields = ['name', 'author', 'cover']