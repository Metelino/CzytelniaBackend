from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Comment(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    text = models.TextField(max_length=1000, default='')
    review = models.BooleanField(default=None)
    book = models.ForeignKey(to='book.Book', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)
    modified = models.BooleanField(default=False)

    def save(self):
        if self.id:
            self.modified = True
        super().save()

    def __str__(self):
        return f'Comment by {self.user} posted at {self.created_at}'

    class Meta:
        ordering = ['created_at']

