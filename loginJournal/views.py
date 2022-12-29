from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def user_login(request):
    return render(request,'login.html',{})
