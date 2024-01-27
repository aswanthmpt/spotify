from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signin(req):
    if req.method=='POST':
        name=req.POST.get('name','')
        email=req.POST.get('email','')
        username=req.POST.get('username','')
        password=req.POST.get('password','')
        cpassword=req.POST.get('cpassword','')
        
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(req,"username alredy exists")
                return redirect('auth:signin')
            elif User.objects.filter(email=email):
                messages.info(req,"email alredy exists")
                return redirect('auth:signin')
            else:
                user=User.objects.create_user(first_name=name,email=email,username=username,password=password)
                user.save()
                print("sign",user)
                return redirect('auth:login')
        else:
            messages.info(req,"pasword doesnote match")
            return redirect('auth:signin')
    return render(req,'usersignin.html')
    
def login(req):
    if req.method=='POST':
        username=req.POST.get('username','')
        password=req.POST.get('password','')
        print(username,password)
        user = auth.authenticate(username=username,password=password)
        print("log",user)
        if user is not None:
            auth.login(req,user)
            return redirect('/')
        else:
            messages.info(req,"invalid details")
            return redirect('auth:login')
    return render(req,"login.html")


def logout(req):
    auth.logout(req)
    return redirect('user:home')