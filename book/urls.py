from django.urls import path
from .views import book_cover, book_page

app_name = 'books'

urlpatterns = [
    path('book_cover/<id>', book_cover),
    path('book_page/<id>', book_page),
]