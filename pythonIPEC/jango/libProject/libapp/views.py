from django.shortcuts import render
from .models import Book
from .form import BookForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'add_book.html', {'form': BookForm(), 'msg': 'Book added successfully!'})
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

def viewbooks(request):
    books = Book.objects.all()
    return render(request, 'viewbooks.html', {'books': books})

def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    books = Book.objects.all()
    return render(request, 'viewbooks.html', {'books': books, 'msg': 'Book deleted successfully!'})