from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    content = models.FileField()
    cover = models.FileField()
    comments = models.ManyToManyField(to='comment.Comment', related_name='book_comments', blank=True)

    def __str__(self):
        return f'{self.name} by {self.author}'
    
    class Meta:
        ordering = ['id']
    # @property
    # def liked(self):
    #     return self.comments.filter(review=True)

    # @property
    # def disliked(self):
    #     return self.comments.filter(review=False)