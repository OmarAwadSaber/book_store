from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Category
from .forms import BookForm

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

def create_book(request):
    if request.method == "POST" : 
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books_list')
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {'form' : form, "message" : "Create New Book"})
    
    
def update_book(request, book_id):
    book = get_object_or_404(Book, id = book_id)
    if request.method == "POST" :
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail',book_id = book_id)
    else:
        form = BookForm(instance=book)
    return render(request, 'books/book_form.html', {'form' : form, "message" : "Update book"})


def delete_book(request, book_id):
    book = get_object_or_404(Book, id = book_id)
    book.delete()
    return redirect('books_list')