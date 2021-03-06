from django.shortcuts import render
from rest_framework import generics
from .serializers import BookSerializer
from django.core.paginator import Paginator
from django.views.generic import ListView
from .models import Book

def home(request):
	return render(request, 'booksiteapp/base.html')

def test(request):
	context = {
        'book': Book.objects.all()
    }
	return render(request, 'booksiteapp/home.html', context)

def searchbar(request):
	if request.method == 'GET':
		search = request.GET.get('search')
		post = Book.objects.all().filter(title = search)
		return render(request, 'booksiteapp/base.html', {'post' : post})

class BookView(generics.ListAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer

class AddBook(generics.CreateAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer

class Browse(ListView):
	model = Book
	template_name = 'booksiteapp/browsing.html'
	context_object_name = 'books'
	ordering = ['price']
	paginate_by =  2