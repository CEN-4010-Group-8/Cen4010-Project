from django.shortcuts import render
from rest_framework import generics
from .serializers import BookSerializer
from .models import Book

def home(request):
	return render(request, 'booksiteapp/home.html')

class BookView(generics.ListAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer