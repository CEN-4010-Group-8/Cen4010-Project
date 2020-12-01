
from django.contrib.auth.models import User
from django.db import models

class Userprofile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    address = models.CharField(max_length=255, blank=True, null=True)
    zipcode = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return '%s' % self.user.username

User.userprofile = property(lambda u:Userprofile.objects.get_or_create(user=u)[0])

class CreditCard(models.Model):
	
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    cardNumber = models.IntegerField(primary_key = True)
    cardFirstName = models.CharField(max_length = 100, null =True)
    cardLastName = models.CharField(max_length = 100, null =True)
    securityCode = models.IntegerField()
    expirationDate = models.IntegerField()
	
def __str__(self):
        return '%s' % self.user.username
        User.creditcard = property(lambda u:CreditCard.objects.get_or_create(user=u)[0])