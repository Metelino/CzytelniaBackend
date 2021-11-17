from ninja import ModelSchema

from .models import Comment

class CommentEditSchema(ModelSchema):
    class Config:
        model = Comment
        model_fields = ['id', 'text', 'review']

class CommentSchema(ModelSchema):
    class Config:
        model = Comment
        model_fields = ['id', 'user', 'text', 'review', 'created_at', 'modified', 'modified_at']
