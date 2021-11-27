from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router
from ninja.errors import HttpError

from book.models import Book
from .models import Comment
from .schemas import CommentEditSchema, CommentSchema
from user.jwt import JWT
from user.models import User

api = Router()

@api.get('get/{book_id}', response={200 : List[CommentSchema]})
def get_comments(request, book_id: int):
    book = get_object_or_404(Book, id=book_id)
    comments = book.comment_set.all()
    return 200, list(comments)

@api.post('post/{book_id}', response={201 : CommentSchema}, auth=JWT())
def create_comment(request, book_id: int, data: CommentEditSchema):
    id = int(request.auth['sub'])
    print(data.dict())
    comm = Comment.objects.create(**data.dict(), book_id=book_id, user_id=id)
    return 201, comm

@api.put('put/{comment_id}', response={204 : None}, auth=JWT())
def update_comment(request, comment_id : int,  data: CommentEditSchema):
    comment = get_object_or_404(Comment, id=comment_id)
    id = int(request.auth['sub'])
    if not comment.user.id == id:
        raise HttpError(404, 'Comment does not belong to this user')
    for attr, value in data.dict().items():
        setattr(comment, attr, value)
    comment.save()
    return 204, None

@api.delete('delete/{comment_id}', response={204 : None}, auth=JWT())
def del_comment(request, comment_id: int):
    comment = get_object_or_404(Comment, id=comment_id)
    # Dodaj sprawdzanie czy comment jest usera
    comment.delete()
    return 204, None