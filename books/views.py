from django.shortcuts import render, get_object_or_404
from .models import Book, Category

def books_list(request):
    books = Book.objects.all()
    
    return render(request, 'books/books_list.html' , {"books_list" : books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id = book_id)
    return render(request, 'books/book_detail.html', {"book" : book})

def category_books(request, category_id):
    category_object = get_object_or_404(Category, id = category_id)
    books = Book.objects.filter(category=category_object)
    return render(request, 'books/category_books.html', {"books" : books, "category" : category_object})