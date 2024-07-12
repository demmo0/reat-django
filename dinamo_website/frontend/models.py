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