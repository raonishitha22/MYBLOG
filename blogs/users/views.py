from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from .forms import loginform,regisform


# Create your views here.
def sign_up(request):
    if request.method =='GET':
        if request.user.is_authenticated:
            return redirect('home')
        form=loginform()
        return render(request,"login.html",{'form':form})
        
    elif request.method=='POST':    
        form=loginform(request.POST)
        
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                messages.success(request,f'Welcome back')
                return redirect('home')
        messages.error(request,f'Invalid username or password')
        context={
            'form':form
        }  
        return render(request,"login.html",context)

def sign_out(request):
    logout(request)
    messages.success(request,f'You have been logged out')
    return redirect('login')

def register(request):
    if request.method=='GET':
        form=regisform()
        return render(request,"regis.html",{'form':form})  
    if request.method=='POST':
        form=regisform(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
            login(request, user)
            return redirect('home')
        else:
            return render(request,'regis.html',{'form':form})