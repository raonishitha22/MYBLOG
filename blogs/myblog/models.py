from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.
#gchoices=((1,Personal),(2,Profesional),(3,Business/corporate),(4,Fashion),(5,Lifestyle),(6,Newsblog),(7,Travel),(8,Food),(9,Review),(10,Multimedia))
class myblog(models.Model):
    Author=models.ForeignKey(User, on_delete=models.CASCADE)
    ID=models.BigAutoField(primary_key=True)
    Title=models.CharField(max_length=40)
    Content=RichTextField()
    published_at=models.DateTimeField(default=timezone.now)
    #genre=models.CharField(choices=gchoices)
    
    def __str__(self):
        return self.Title
    
    class Meta:
        ordering=['-published_at']
    
    def noof_comments(self):
        return BlogComment.objects.filter(blog=self).count()    

class BlogComment(models.Model):
    blog=models.ForeignKey(myblog,related_name='comments',on_delete=models.CASCADE)  
    content=models.TextField()
    Author=models.ForeignKey(User,on_delete=models.CASCADE)
    date_posted=models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.blog.Title

    
    