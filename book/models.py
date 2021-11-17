from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200, default='')
    author = models.CharField(max_length=200, default='')
    content = models.FileField()
    cover = models.FileField()
    summary = models.CharField(max_length=1000, default='')
    comments = models.ManyToManyField(to='comment.Comment', related_name='book_comments', blank=True)

    def __str__(self):
        return f'{self.title} by {self.author}'
    
    class Meta:
        ordering = ['id']

    @property
    def liked(self) -> int:
        return self.comments.filter(review=True).count()

    @property
    def disliked(self) -> int:
        return self.comments.filter(review=False).count()