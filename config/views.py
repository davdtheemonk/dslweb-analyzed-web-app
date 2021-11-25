from django.contrib.auth import authenticate,login,logout
from django.http import request
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def user_login(request):
    if request.method =='POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user= authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return  redirect('home')
        else:
            messages.error(request,"Incorrect username or password")
            return render(request,'login.html')
           
            
           
    else :
        
         return render(request,'login.html', {'error_message': 'Something went wrong.Try Again'})
    
def logout_user(request):
	logout(request)
	messages.success(request,"You have succefully logged out")
	return render(request,'home.html')
@login_required
def profile(request):
    return render(request,'profile.html')
