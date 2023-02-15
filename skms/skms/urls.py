from django.urls import path
from . import views

urlpatterns = [
    path('sign-in/', views.index),
    path('sign-up/', views.createAccount),
]