from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        pw=request.POST['password']
        user=auth.authenticate(username=username,password=pw)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid user")
            return redirect('login')
    return render(request,"loginpage.html")
def new(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        password = request.POST['password']
        confirmpassword = request.POST['password1']

        if password==confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username is taken")
                return redirect('new')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"the email is used")
                return redirect('new')
            else:
               ucer=User.objects.create_user(username=username,email=email,password=password,first_name=firstname,last_name=lastname)
               ucer.save()
               print("successful")
               return redirect('login')
        else:
              messages.info(request,"password not matching")
              return redirect('new')

    return render(request,"theone.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

