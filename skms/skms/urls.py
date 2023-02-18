from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.index, name='index'),
    path('sign-up/', views.createAccount),
    path('user-profile/', views.userProfile),
]
