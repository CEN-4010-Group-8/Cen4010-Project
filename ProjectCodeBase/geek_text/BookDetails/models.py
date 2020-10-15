from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    
    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

class Genre(models.Model):
    topic = models.CharField(max_length=20)

    def __unicode__(self):
        return self.topic

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    rating = models.IntegerField()
    release_date = models.DateField()
    top_seller = models.BooleanField()

    def __unicode__(self):
        return self.title