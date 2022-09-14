from contextlib import redirect_stderr
from urllib import request
from django.shortcuts import redirect, render
import authentication
from .forms import NewUserForm
from django.contrib.auth import login,authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.


def register_request(request):
    if request.method =="POST":
        form  = NewUserForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successfull.")
            return redirect("authentication/login.html")
        
        messages.error(request,"Unsuccessfull login!")
    
    form = NewUserForm()        
    return render(request=request, template_name="authentication/register.html", context={"register_form":form})



def login_request(request):
    if request.method =='POST':
        
        form  = AuthenticationForm(request, request.POST)
        
        if form.is_valid:
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('passowrd')
            
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are logged in as {username}.")
                return redirect ('main/home.html')
            else:
                messages.error(request, "Invalid username or password")
        else:
            
            messages.error(request, "You dont have an account")
            
    form = AuthenticationForm()
    return render(request, "authentication/login.html",context = {'login_form': form})
            
            
            