from django.shortcuts import render
from django.http import HttpResponse

from django.views import generic

from .models import Book, Author, BookInstance, Genre

def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_authors = Author.objects.all().count()
    num_copies = BookInstance.objects.all().count()
    num_copies_available = BookInstance.objects.filter(status='a').count()

    return render(
      request,
      'index.html',
      context = {
        'num_books':num_books, 
        'num_instances':num_books, 
        'num_authors':num_authors, 
        'num_copies':num_copies,
        'num_copies_available':num_copies_available
      }
    )

class BookListView(generic.ListView):
    model = Book
    context_object_name = 'Buchliste'
    paginate_by = 10
   
class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    context_object_name = 'Autorenliste'

class AuthorDetailView(generic.DetailView):
    model = Author
