from django.shortcuts import render
from .forms import BookForm
from .models import Book, Author, Genre

def home(request):
    return render(request, 'books/home.html')

def genre_books(request):
    genres = Genre.objects.all()  
    selected_genre = request.GET.get('genre')  
    books = Book.objects.filter(genre__name=selected_genre) if selected_genre else None
    return render(request, 'books/genre_books.html', {'genres': genres, 'books': books})

def author_genres(request):
    last_name = request.GET.get('last_name')  
    genres = None
    authors = Author.objects.filter(last_name=last_name) 

    if authors.exists(): 
        genres = Genre.objects.filter(books__author__in=authors).distinct()  

    return render(request, 'books/author_genre.html', 
        {'genres': genres,
        'last_name': last_name,
        'authors': authors, })
    
def first_books(request):
    books = Book.objects.all()[:5]
    return render(request, 'books/first_books.html', {'books': books})
