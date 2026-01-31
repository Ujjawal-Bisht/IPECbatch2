from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .serializers import BookSerializer
from rest_framework import generics

# Create your views here.
def home(request):
    return render(request, 'home.html')

@login_required
def addbook(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'addbook.html', {'form': BookForm(), 'msg': 'Book added successfully!'})
    else:
        form = BookForm()
    return render(request, 'addbook.html', {'form': form})

@login_required
def viewbooks(request):
    bookdata = Book.objects.all()
    return render(request, 'viewbooks.html', {'bookdata': bookdata})

@login_required
def deletebook(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    bookdata = Book.objects.all()
    return render(request, 'viewbooks.html', {'bookdata': bookdata, 'msg': 'Book deleted successfully!'})

@login_required
def searchbook(request):
    if request.method == "POST":
        id = request.POST.get('id')
        book = Book.objects.get(id=id)
        return render(request, 'searchbook.html', {'book': book})
    
    return render(request, 'searchbook.html')


def signup(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST) #Create an object of UserCreationForm
        if form.is_valid():
            form.save()
            return render(request,'signup.html',{'form':UserCreationForm(),'msg':'User created successfully!'})
    else:
        form=UserCreationForm()
    return render(request,'signup.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'form': form, 'msg': 'Invalid credentials!'})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer