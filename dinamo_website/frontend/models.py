from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class React(models.Model):
    employee = models.CharField(max_length=30)
    department = models.CharField(max_length=30)
    
class CustomUser(AbstractUser):
    authorization = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Article(models.Model):
    
    title = models.CharField(max_length=150,blank=True)
    image = models.ImageField(blank=True)
    article = models.TextField(null=True,blank=True)
    order = models.CharField(max_length=5)
    active = models.BooleanField(default=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    
