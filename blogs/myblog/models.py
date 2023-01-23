from django.db import models

# Create your models here.
class myblog(models.Model):
    Name=models.CharField(max_length=40)
    ID=models.BigAutoField(primary_key=True)
    Title=models.CharField(max_length=40)
    Description=models.TextField(blank=False,default=" ")
    
    