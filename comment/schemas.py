from ninja import ModelSchema

from .models import Comment
from user.schemas import UserOut

# class CommentCreateSchema(ModelSchema):
#     class Config:
#         model = Comment
#         model_fields = ['text', 'review']

class CommentEditSchema(ModelSchema):
    class Config:
        model = Comment
        model_fields = ['text', 'review']

class CommentSchema(ModelSchema):
    user : UserOut
    class Config:
        model = Comment
        model_exclude = ['user']
        #model_fields = ['id', 'user', 'text', 'review', 'created_at', 'modified', 'modified_at']
