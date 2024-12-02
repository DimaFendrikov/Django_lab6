from django.urls import path
from . import views

urlpatterns = [
    path('first_books/', views.first_books, name='first_books'),  
    path('genre_books/', views.genre_books, name='genre_books'), 
    path('author_genres/', views.author_genres, name='author_genres'), 
]
