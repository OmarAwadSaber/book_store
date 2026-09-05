from django.urls import path
from .views import books_list, book_detail, category_books, create_book, update_book, delete_book
urlpatterns = [
    path('', books_list, name="books_list"),
    path('<int:book_id>/', book_detail, name="book_detail"),
    path('category/<int:category_id>/', category_books, name="category_books"),
    path('create/', create_book, name="create_book"),
    path('<int:book_id>/update/', update_book, name="update_book"),
    path('<int:book_id>/delete/', delete_book, name="delete_book"),
]