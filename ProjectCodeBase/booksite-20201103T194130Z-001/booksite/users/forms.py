from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Userprofile, CreditCard

class UserRegisterForm(UserCreationForm):
    
    first_name = forms.CharField(max_length=30, required=False, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Required.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email','password1', 'password2']
        
class UserprofileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserprofileForm, self).__init__(*args, **kwargs)

        self.fields['address'].widget.attrs['class'] = 'input'
        self.fields['zipcode'].widget.attrs['class'] = 'input'
        self.fields['place'].widget.attrs['class'] = 'input'
        self.fields['phone'].widget.attrs['class'] = 'input'

    class Meta:
        model = Userprofile
        fields = '__all__'
        exclude = ('user',)


class CreditCardForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreditCardForm, self).__init__(*args, **kwargs)

        self.fields['cardNumber'].widget.attrs['class'] = 'input'
        self.fields['cardFirstName'].widget.attrs['class'] = 'input'
        self.fields['cardLastName'].widget.attrs['class'] = 'input'
        self.fields['securityCode'].widget.attrs['class'] = 'input'
        self.fields['expirationDate'].widget.attrs['class'] = 'input'

    class Meta:
        model = CreditCard
        fields = '__all__'
        exclude = ('user',)
        
        