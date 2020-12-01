from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import  UserRegisterForm, UserprofileForm, CreditCardForm
from .models import Userprofile, CreditCard



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def account(request):
    return render(request, 'users/account.html')
def Userprofile(request):
    if request.method == 'POST':
        userprofile = UserprofileForm(request.POST)
        
        if userprofile.is_valid():  
            userprofile=userprofile.save()

            

            Name = userprofile.cleaned_data.get('first_name')
            return redirect('users/account.html')

    else:
        userprofile = UserprofileForm(),

    return render(request, 'users/login.html', {'form': form })
def CreditCard(request):
    if request.method == 'POST':
        creditcard = CreditCardForm(request.POST)
        
        if creditcard.is_valid():  
            creditcard=creditcard.save()

            

            username= creditcard.cleaned_data.get('username')
            return redirect('users/account.html')

    else:
        creditcard = CreditCard(),

    return render(request, 'users/login.html', {'form': form })
