from django.contrib.auth import authenticate,login
from django.http import request
from django.shortcuts import render,redirect
from django.contrib import messages

def user_login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user= authenticate(request,userame=username,password=password)
        if user is not None:
            login(request,user)
            return  render(request,'home.html')
        else:
        	messages.success(request,('Incorrect username and / or password'))
            return redirect('logon.html')
    else :
        return render(request,'login.html')
    

