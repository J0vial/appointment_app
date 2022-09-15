from contextlib import redirect_stderr
from urllib import request
from django.shortcuts import redirect, render
from django.contrib.auth import login,authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import additionUserInfoForm,NewUserForm
from .models import additionalUserInfo
from django.contrib.auth.models import User

# Create your views here.


def register_request(request):
    if request.method =="POST":
        form  = NewUserForm(request.POST)
        extend_form = additionUserInfoForm(request.POST)
        
        if form.is_valid() and extend_form.is_valid():
            user = form.save()
            
            extend_profile = extend_form.save(commit=False)
            extend_profile.user = user
            extend_profile.save()
            
            login(request, user)
            messages.success(request, "Registration successfull.")
            return redirect("authentication:login")
        
        messages.error(request,"Unsuccessfull login!")
    else:
    
        form = NewUserForm()   
        extend_form = additionUserInfoForm()
      
    return render(request=request, template_name="authentication/register.html", context={"register_form":form,'extend_form':extend_form})



def login_request(request):
    if request.method =='POST':
        
        form  = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are logged in as {username}.")
                user_table = User.objects.filter(username = username).values('id')
                user_table_2 = User.objects.get(pk=user_table[0]['id'] )
                additional = user_table_2.additionaluserinfo.catagory
                
                if additional =='Doctor':
                    
                    return redirect ('main:doctor')
                else:
                    return redirect ('main:patient')
                    
            else:
                messages.error(request, "Invalid username or password")
        else:
            
            messages.error(request, "You dont have an account")
    else:
            
        form = AuthenticationForm()
    return render(request, "authentication/login.html",context = {'login_form': form})
            
            
            