from django.shortcuts import render, get_object_or_404,redirect
from .models import myblog
from .forms import blogform,regisform,loginform
from django.contrib import messages
from django.contrib.auth import login,authenticate, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home_view(request):
    myblogs=myblog.objects.all()
    context={
        'blogs': myblogs
    }
    return render(request,'home.html',context)

@login_required
def blog_create_view(request):
    if request.method=='GET':
        con={'form':blogform()}
        return render(request,'blog_create.html',con)
    elif request.method=='POST':   
        form=blogform(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.Author=request.user
            form.save()
            form=blogform()
            messages.success(request,'The post has been created successfully')
    context={
        'form':form
    }    
    return render(request,"blog_create.html",context)

@login_required
def blog_delete_view(request,ID):
    queryset=myblog.objects.filter(Author=request.user)
    obj=get_object_or_404(queryset,ID=ID)
    context={
        'obj':obj
    }
    if request.method=='GET':
        return render(request,"blog_delete.html",context) 
    elif request.method=='POST':
        obj.delete()
        messages.success(request,'your post is deleted successfully')
        return redirect('home')
    
   
    return render(request,"blog_delete.html",context) 

@login_required
def dynamic_view(request,id):
    obj=get_object_or_404(myblog,ID=id)
    context={
        "obj":obj
    }
    return render(request,"blog_dynamic.html",context)


@login_required
def blog_update_view(request,id):
    queryset=myblog.objects.filter(Author=request.user)
    obj=get_object_or_404(myblog,ID=id)
    if request.method == 'GET':
        context = {'form': blogform(instance=obj), 'id': id}
        return render(request,'blog_update.html',context) 
    elif request.method=='POST': 
        form=blogform(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request,'Your post is updated')  
            return redirect('posts')
        else:
            return render(request,'blog_update.html',{'form':form})
        


    
    