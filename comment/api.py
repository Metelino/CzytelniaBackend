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

@api.get('{book_id}', response={200 : List[CommentSchema]})
def get_comments(request, book_id: int):
    book = get_object_or_404(Book, id=book_id)
    comments = book.comment_set.all()
    return 200, list(comments)

@api.get('{book_id}/user', response={200 : CommentSchema, 204 : None}, auth=JWT())
def get_comments(request, book_id: int):
    user_id = int(request.auth['sub'])
    book = get_object_or_404(Book, id=book_id)
    comment = book.comment_set.filter(user_id = user_id)
    if comment.exists():
        return 200, comment.first()
    return 204, None

@api.post('{book_id}', response={201 : CommentSchema}, auth=JWT())
def create_comment(request, book_id: int, data: CommentEditSchema):
    id = int(request.auth['sub'])
    print(data.dict())
    try:
        comm = Comment.objects.create(**data.dict(), book_id=book_id, user_id=id)
        return 201, comm
    except:
        raise HttpError(409, "Review already exists")

@api.put('{book_id}', response={204 : None}, auth=JWT())
def update_comment(request, book_id : int,  data: CommentEditSchema):
    id = int(request.auth['sub'])
    try:
        comm = Comment.objects.get(book_id=book_id, user_id=id)
        for attr, value in data.dict().items():
            setattr(comm, attr, value)
        comm.save()
    except:
        Comment.objects.create(**data.dict(), user_id=id, book_id=book_id)
    return 204, None

# @api.api_operation(["POST", "PATCH"], 'edit/{book_id}', response={204 : None}, auth=JWT())
# def update_comment(request, book_id : int,  data: CommentEditSchema):
#     user_id = int(request.auth['sub'])
#     if request.method == "POST":
#         comm = Comment.objects.get(user_id=user_id, book_id=book_id)
#         for attr, value in data.dict().items():
#             setattr(comm, attr, value)
#         comm.save()
#     if request.method == 
#         comm = Comment.objects.create(**data.dict(), book_id=book_id, user_id=id)
#     return 204, None

@api.delete('{book_id}', response={204 : None}, auth=JWT())
def del_comment(request, book_id: int):
    user_id = int(request.auth['sub'])
    comment = get_object_or_404(Comment, book_id=book_id, user_id=user_id)
    comment.delete()
    return 204, None

# @api.put('put/{comment_id}', response={204 : None}, auth=JWT())
# def update_comment(request, comment_id : int,  data: CommentEditSchema):
#     comment = get_object_or_404(Comment, id=comment_id)
#     id = int(request.auth['sub'])
#     if not comment.user.id == id:
#         raise HttpError(404, 'Comment does not belong to this user')
#     for attr, value in data.dict().items():
#         setattr(comment, attr, value)
#     comment.save()
#     return 204, None

# @api.delete('delete/{comment_id}', response={204 : None}, auth=JWT())
# def del_comment(request, comment_id: int):
#     comment = get_object_or_404(Comment, id=comment_id)
#     # Dodaj sprawdzanie czy comment jest usera
#     comment.delete()
#     return 204, None