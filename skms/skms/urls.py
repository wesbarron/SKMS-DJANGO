from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('sign-up/', views.createAccount),
    path('user-profile/', views.userProfile),
    path('forum/', views.forum, name='forum'),
    path('forum/create-post/', views.renderCreatePost),
    path('forum/create-post/create', views.createPost),
    path('forum/post/<int:post_id>/', views.post, name='post'),
     path('submit-comment/<int:post_id>', views.createComment, name='create-comment'),
     path('forum/sort=<str:sort>', views.sort_by, name='sort-by'),
     path('forum/filter=<str:subject>', views.filterSubject, name='filter-subject'),

]