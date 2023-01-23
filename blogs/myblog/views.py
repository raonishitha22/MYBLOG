from django.shortcuts import render, get_object_or_404
from .models import myblog
from .forms import blogform
# Create your views here.
def blog_create_view(request):
    form=blogform(request.POST or None)
    if form.is_valid():
        form.save()
        form=blogform()
    context={
        'form':form
    }    
    return render(request,"blog_create.html",context)

def blog_delete_view(request,ID):
    obj=get_object_or_404(myblog,ID=ID)
    if request.method=='POST':
        obj.delete()
    context={
        'obj':obj
    }
   
    return render(request,"blog_delete.html",context) 

def dynamic_view(request,id):
    obj=get_object_or_404(myblog,ID=id)
    context={
        "obj":obj
    }
    return render(request,"blog_dynamic.html",context)
    
    