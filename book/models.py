from django.db import models
from django.dispatch import receiver
from django.urls import reverse_lazy

class Book(models.Model):
    title = models.CharField(max_length=200, default='')
    author = models.CharField(max_length=200, default='')
    content = models.FileField()
    cover = models.FileField()
    content_url = models.CharField(max_length=200, default='', blank=True, editable=False)
    summary = models.CharField(max_length=1000, default='',)

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

# @receiver(models.signals.post_save, sender=Book)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         instance.content_url = reverse_lazy("api-1.0.0:pdf", kwargs={"book_id":instance.id})
#         instance.save()

@receiver(models.signals.post_init, sender=Book)
def create_user_profile(sender, instance, **kwargs):
    instance.content_url = reverse_lazy("api-1.0.0:pdf", kwargs={"book_id":instance.id})
    #instance.save()