from django.urls import path
from .views import book_cover, book_page

app_name = 'books'

urlpatterns = [
    path('book_cover/<book_id>', book_cover),
    path('book_page/<book_id>', book_page),
]