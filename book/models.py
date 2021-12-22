from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200, default='')
    author = models.CharField(max_length=200, default='')
    content = models.FileField()
    cover = models.FileField()
    summary = models.CharField(max_length=1000, default='')

    def __str__(self):
        return f'{self.title} by {self.author}'
    
    class Meta:
        ordering = ['id']

    def get_liked(self) -> int:
        return self.comment_set.filter(review=True).count()

    def get_disliked(self) -> int:
        return self.comment_set.filter(review=False).count()

    liked = property(get_liked)
    disliked = property(get_disliked)

# @receiver(post_save, sender=Book)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         instance.cover = reverse_lazy("api-1.0.0:cover", kwargs={"book_id":instance.id})
#         instance.content = reverse_lazy("api-1.0.0:pdf", kwargs={"book_id":instance.id})
#         instance.save()