from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.SignUp.as_view(), name="sign-up")
]
