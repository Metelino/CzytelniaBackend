from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router
from ninja.errors import HttpError

from book.models import Book
from .models import Comment
from .schemas import CommentEditSchema, CommentSchema
from user.jwt import JWT

api = Router()

@api.get('get/{book_id}', response=List[CommentSchema])
def get_comments(request, book_id: int):
    book = get_object_or_404(Book, id=book_id)
    comments = book.comment_set.all()
    return list(comments)

@api.post('post/{book_id}', auth=JWT())
def create_comment(request, book_id: int, data: CommentEditSchema):
    comm = Comment.objects.create(**data.dict, book=book_id, user=request.user)
    return {'id': comm.id}

@api.put('put/{comment_id}', auth=JWT())
def update_comment(request, comment_id: int, data: CommentEditSchema):
    comment = get_object_or_404(Comment, id=comment_id)
    id = int(request.auth['sub'])
    if not comment.user.id == id:
        raise HttpError(404, 'Comment does not belong to this user')
    for attr, value in data.dict().items():
        setattr(comment, attr, value)
    return {'success': True}

@api.delete('delete/{comment_id}', auth=JWT())
def del_comment(request, comment_id: int):
    comment = get_object_or_404(Comment, id=comment_id)
    # Dodaj sprawdzanie czy comment jest usera
    comment.delete()
    return {'success': True}