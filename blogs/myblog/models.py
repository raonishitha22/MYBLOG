from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class myblog(models.Model):
    Author=models.ForeignKey(User, on_delete=models.CASCADE)
    ID=models.BigAutoField(primary_key=True)
    Title=models.CharField(max_length=40)
    Content=models.TextField(blank=False,default=" ")
    published_at=models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.Title
    
    class Meta:
        ordering=['-published_at']
    

    
    