from django.shortcuts import render, get_object_or_404,redirect
from .models import myblog,BlogComment
from .forms import blogform,regisform,loginform,commentform
from django.contrib import messages
from django.contrib.auth import login,authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.views import generic
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
@login_required
def home_view(request):
    myblogs=myblog.objects.filter(Author=request.user)
    context={
        'blogs': myblogs
    }
    return render(request,'home.html',context)
@login_required

def allposts(request):
    allblogs=myblog.objects.all()
    context={
        'blogs' : allblogs
    }
    return render(request,'allposts.html',context)

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
def dynamic_view(request,ID):
    obj=get_object_or_404(myblog,ID=ID)
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
            return redirect('home')
        else:
            return render(request,'blog_update.html',{'form':form})
        
@login_required
def post_detail(request,ID):
    template_name='blog_dynamic.html'
    post=get_object_or_404(myblog,ID=ID)
    comments=BlogComment.objects.filter(blog_id=ID)
    #comment_form=commentform(data=request.POST)
    new_comment=None
    if request.method=='POST':
        comment_form=commentform(data=request.POST)
        
        if comment_form.is_valid():
           # Author=request.User
            new_comment=comment_form.save(commit=False)
            new_comment.Author=request.user
            new_comment.blog=post
            new_comment.save()
            #context={'form':form}
            new_comment=None
            comment_form=commentform()
        
    else:
        comment_form=commentform()
    context={'post':post,'comment_form':comment_form,'comments':comments,'new_comment':new_comment}    
    return render(request,'blog_dynamic.html',context)      

@login_required
def search(request):
    if request.method=='POST':
        name=request.POST.get('name',None)
        if name:
            result=myblog.objects.filter(Title__icontains=name)
            return render(request,'search.html',{"results":result})
        else:
            messages.success(request,'Search not found')
            return redirect('allposts')
        
       
    else:
        blogs=myblog.objects.all()
        context={
            'blogs':blogs
        }
        return render(request,'search.html',context)
        












































