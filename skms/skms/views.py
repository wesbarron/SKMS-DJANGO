from django.contrib.auth import forms  
from django.shortcuts import redirect, render  
from django.contrib import messages  
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm  
from .signUpForm import username_clean, email_clean
from .models import UserAccount



# Create your views here.from django.http import HttpResponse


def index(request):
    if request.method == 'POST':
        username = request.POST['user_name'].lower() 
        password = request.POST['password'] 
        print(username, password)
        userNameCheck = UserAccount.objects.filter(username = username).exists()
        userPasswordCheck = UserAccount.objects.filter(password=password, username=username).exists()
        print(userNameCheck, userPasswordCheck)
        context = {"username":username}
        if userNameCheck == True and userPasswordCheck == True:
            return render(request, 'user-profile.html', context=context)
        else:
            messages.error(request, 'The username or password combination is incorrect.')
            return render(request, 'sign-in.html')

    return render(request, 'sign-in.html')
    

def createAccount(request):
    if request.method == 'POST': 
        first_name = request.POST['first_name']
        last_name = request.POST['last_name'] 
        email = request.POST['email'] 
        username = request.POST['user_name'] 
        password = request.POST['password'] 
        userNameCheck = User.objects.filter(username = username).exists()
        if userNameCheck == True:
            print(userNameCheck)
            messages.error(request, 'The username '+username+' already exists.')
            return render(request, 'sign-up.html')
        else:
            ins = User.objects.create_user(first_name = first_name, last_name = last_name, email = email, username = username, password = password)
            ins.save()
            ins2 = UserAccount(firstname = first_name, lastname = last_name, email = email, username=username, password=password, status='Active', type='User')
            ins2.save()
            messages.success(request, 'The account was successfully created.')
            return render(request, 'sign-up.html')
              
    return render(request, 'sign-up.html')

def userProfile(request):
    if request.method == 'POST':
        username = request.POST['user_name'] 
        password = request.POST['password'] 
        userNameCheck = User.objects.filter(username = username).exists()
        passwordCheck = User.objects.filter(password = password).exists()
        context = {"username":username}
        if userNameCheck == True and passwordCheck == True:
            return render(request, 'user-profile.html', username = username)
        else:
            return render(request, 'sign-in.html')

    return render(request, 'user-profile.html')