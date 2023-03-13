from django.contrib.auth import forms  
from django.shortcuts import redirect, render  
from django.contrib import messages  
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm  
from .signUpForm import username_clean, email_clean
from .models import *

from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import JsonResponse
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder





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

def forum(request):
    posts = Post.objects.all()
    subjects = Subject.objects.all()
    return render(request, "discussion-home.html", {'posts':posts, 'subjects':subjects})

def sort_by(request, sort):
    if(sort=='Likes'):
        annotated_posts = Post.objects.annotate(
        like_count=Count('likes'))
        # Order the annotated posts by like count
        sorted_posts = annotated_posts.order_by('-like_count')
        # Serialize the filtered and sorted posts as JSON data
        data = serializers.serialize('json', sorted_posts, fields=('id', 'title', 'author', 'datetime', 'likes', 'comments', 'subject'))
        # Return the serialized data as a JSON response
    if(sort=='Comments'):
        annotated_posts = Post.objects.annotate(
        comment_count=Count('comments'))
        # Order the annotated posts by like count
        sorted_posts = annotated_posts.order_by('-comment_count')
        # Serialize the filtered and sorted posts as JSON data
        data = serializers.serialize('json', sorted_posts, fields=('id', 'title', 'author', 'datetime', 'likes', 'comments', 'subject'))
        # Return the serialized data as a JSON response
    return JsonResponse({'data': data})

def filterSubject(request, subject):
    print(subject)
    filtered_posts = Post.objects.filter(subject=subject)
    subjects = Subject.objects.all()

    return render(request, "discussion-home.html", {'posts':filtered_posts, 'subjects':subjects,'selected_subject': subject})

def post(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, "post.html", {'post':post})


def renderCreatePost(request):
    subjects = Subject.objects.all()
    return render(request,"create-post.html", {'subjects': subjects})

def createTestPost():
    author = User.objects.get(username='katiea')
    post1 = Post(title='This is another test post',
        content='This is test content.',
        author=author,
        datetime = timezone.now(),
        subject="TestSubject",
        likes=4
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
        subject = request.POST['subject']
        
        newPost = Post(title=title, content=content, author=author, datetime=datetime, subject=subject)
        newPost.save()
        return redirect('forum')
def likePost(request, post_id):
    if request.method == 'POST':
        post = Post.objects.get(id=post_id)
        post.likes += 1
        post.save()
        return JsonResponse({'likes': post.likes})

#@login_required
def createComment(request, post_id):
     if request.method == 'POST': 
        post = Post.objects.get(id=post_id)
        author = request.user
        content = request.POST['content']
        datetime = timezone.now()
        
        newComment = Comment(post=post, content=content, author=author, datetime=datetime)
        newComment.save()
        return redirect('post', post_id=post_id)

#@login_required
def home(request):
    return render(request, "home.html")