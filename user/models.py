from django.db import models
from django.contrib import auth

from django.db.models.signals import post_save
from django.dispatch import receiver

class User(auth.models.User):
    
    def __str__(self):
        return "@{}".format(self.username)

class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    books = models.ManyToManyField(to='book.Book')

    def __str__(self):
        return f'{self.user.username}\'s profile'

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
