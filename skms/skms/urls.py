from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('sign-up/', views.createAccount),
    path('user-profile/', views.userProfile),
    path('forum/', views.forum, name='forum'),
    path('forum/create-post/', views.renderCreatePost),
    path('forum/create-post/create', views.createPost),
    path('forum/post/<int:post_id>/', views.post, name='post')

]