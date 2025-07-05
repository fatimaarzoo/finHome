from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    role_choices=(
        ('student','Student'),
        ('renter','Renter'),
        ('seller','Seller')
    )
    role=models.CharField(max_length=20,choices=role_choices)
    phone=models.CharField(max_length=10,blank=True)
    email=models.EmailField(max_length=10,blank=True)
    address=models.CharField(max_length=400,blank=True)
    gov_id=models.FileField(blank=True)

    def __str__(self):
        return f"{self.username} ({self.role}) ({self.phone})"
    
class UserProfile(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    uni=models.CharField(max_length=100)
    image=models.ImageField(default='default.jpg',upload_to='profile_pics')
   
    def __str__(self):
        return self.user.username
    
class RenterProfile(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    building=models.CharField(max_length=100)
    image=models.ImageField(default='default.jpg',upload_to='profile_pics')
    
    def __str__(self):
        return self.user.username
    
class SellerProfile(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    service=models.CharField(max_length=100)
    image=models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return self.user.username
    
    
    
