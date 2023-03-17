from django.contrib import admin
from .models import myblog,BlogComment
# Register your models here.
admin.site.register(myblog)
admin.site.register(BlogComment)