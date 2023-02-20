from django.contrib.auth import forms  
from django.shortcuts import redirect, render  
from django.contrib import messages  
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm  
from .signUpForm import username_clean, email_clean
from skms.models import *
from django.utils import timezone
from django.contrib.auth.decorators import login_required


# Create your views here.from django.http import HttpResponse

def index(request):
    #if user is logged in, return our designated home page, else return to sign in 
    return redirect('sign-in/')
def signIn(request):
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
            messages.success(request, 'The account was successfully created.')
            return render(request, 'sign-up.html')
              
    return render(request, 'sign-up.html')

def profile(request):
    return render(request, "profile.html")

def forum(request):
    posts = Post.objects.all()
    return render(request, "discussion-home.html", {'posts':posts})

def post(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, "post.html", {'post':post})


def renderCreatePost(request):
    return render(request,"create-post.html")

def createTestPost():
    author = User.objects.get(username='katieavt')
    post1 = Post(title='This is a test post',
        content='This is test content.',
        author=author,
        datetime = timezone.now(),
        subject="TestSubject"
    )
    post1.save()
    return post1

@login_required
def createPost(request):
    if request.method == 'POST': 
        title = request.POST['title']
        content = request.POST['description'] 
        author = request.user
        datetime = timezone.now()
        subject = "Null Subject"
        
        newPost = Post(title=title, content=content, author=author, datetime=datetime, subject=subject)
        newPost.save()
        return redirect('forum')
