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
	#ordering = ['rating']
	paginate_by =  40
	def get_queryset(self):
		queryset = Book.objects.all()
		
		choice = self.request.GET.get("featured")
			
		browse = self.request.GET.get("browse")
		stars =  self.request.GET.get("stars")
		seller = self.request.GET.get("Bsort")
		print(browse)
		print(choice)
		print(stars)
		print(seller)
		
		print(browse == "Textbook")
		
		
		
		if browse == "Textbook":
			queryset = queryset.filter(genre = "textbook")
		if browse == "Fiction":
			queryset = queryset.filter(genre = "Fiction")
		if browse == "Sci-Fi":
			queryset = queryset.filter(genre = "Sci-Fi")
		if browse == "Computer Science":
			queryset = queryset.filter(genre = "Computer Science")
			
		
		
		if stars == "1":
			queryset = queryset.filter(rating = '1')
		if stars == "2":
			queryset = queryset.filter(rating = '2')
		if stars == "3":
			queryset = queryset.filter(rating = '3')
		if stars == "4":
			queryset = queryset.filter(rating = '4')
		if stars == "5":
			queryset = queryset.filter(rating = '5')
			
		"""if ((browse!=None or stars!=None):
			if choice """
			
		if seller == "Best Seller":
			queryset = queryset.filter(topSeller = True)
			
		print(choice)
		print(choice == "Price")
		if choice == "Price":
			queryset = queryset.order_by('price')
		elif choice == "Author":
			queryset = queryset.order_by('authorName')
		elif choice == "Title":
			queryset = queryset.order_by('bookTitle')
		elif choice == "Book Rating":
			queryset = queryset.order_by('rating')
		elif choice == "Release Date":
			queryset = queryset.order_by('releaseDate')
			
	
			
		return queryset
	context_object_name = 'books'