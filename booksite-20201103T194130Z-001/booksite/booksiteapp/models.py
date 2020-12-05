from django.db import models


	
	
class Author(models.Model):
	authorId = models.IntegerField(primary_key = True)
	authorName = models.CharField(max_length = 100, null =True)

	def __str__(self):
		return self.authorName
	
	
	

class Publisher(models.Model):
	publisherId = models.IntegerField(primary_key = True)
	publisherName = models.CharField(max_length = 100, null =True)
	authors = models.ManyToManyField(Author)
	
class Book(models.Model):
	bookId = models.IntegerField(primary_key = True)
	bookTitle = models.CharField(max_length = 100, null =True)
	authorName = models.CharField(max_length = 100, null =True)
	publisherName = models.CharField(max_length = 100, null =True)
	publisher = models.ManyToManyField(Publisher)
	author = models.ManyToManyField(Author)
	genre = models.CharField(max_length = 100, null =True)
	price = models.IntegerField()
	rating = models.IntegerField()
	releaseDate = models.DateTimeField()
	topSeller = models.BooleanField()
	
	def __str__(self):
		return self.bookTitle
	


class SiteUser(models.Model):
	userId = models.IntegerField(primary_key = True)
	firstName = models.CharField(max_length = 100, null =True)
	lastName = models.CharField(max_length = 100, null =True)
	email = models.CharField(max_length = 100, null =True)
	userName = models.CharField(max_length = 100, null =True)

class Comment(models.Model):
	commentId = models.IntegerField(primary_key = True)
	commentContent = models.TextField()
	book = models.ForeignKey(Book, on_delete = models.CASCADE)
	siteUser = models.ForeignKey(SiteUser, on_delete = models.CASCADE)

	
class Address(models.Model):
	adressId = models.IntegerField(primary_key = True)
	streetName = models.CharField(max_length = 100, null =True)
	city = models.CharField(max_length = 100, null =True)
	state= models.CharField(max_length = 100, null =True)
	country = models.CharField(max_length = 100, null =True)
	zip = models.IntegerField()
	siteUser = models.ForeignKey(SiteUser, on_delete = models.CASCADE)

class CreditCard(models.Model):
	cardNumber = models.IntegerField(primary_key = True)
	siteUser = models.ForeignKey(SiteUser, on_delete = models.CASCADE)
	cardFirstName = models.CharField(max_length = 100, null =True)
	cardLastName = models.CharField(max_length = 100, null =True)
	securityCode = models.IntegerField()
	expirationDate = models.IntegerField()
	
class ShoppingCart(models.Model):
	subtotal = models.IntegerField()
	siteUser = models.OneToOneField(SiteUser, primary_key = True, on_delete = models.CASCADE)
	
class OrderId(models.Model):
	OrderId = models.IntegerField(primary_key = True)
	ShoppingCart = models.ForeignKey(ShoppingCart, on_delete = models.CASCADE)
	Book = models.ForeignKey(Book, on_delete = models.CASCADE)
	quantity = models.IntegerField()
	
	


	

	
	

	
