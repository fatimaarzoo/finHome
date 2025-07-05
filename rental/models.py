from django.db import models
from django.utils import timezone
from accounts.models import *

class Rcategory(models.Model):
    rtype=models.CharField(max_length=20)
    desp=models.TextField(blank=True)

    def __str__(self):
     return self.rtype
    
class Location(models.Model):
    area=models.CharField(max_length=100)
    pincode=models.DecimalField(max_digits=6,decimal_places=0)
    latitude=models.CharField(max_length=20,blank=True)
    longitude=models.CharField(max_length=20,blank=True)

    def __str__(self):
      return self.area
    
class Attributes(models.Model):
   facilities=models.CharField(max_length=200)

   def __str__(self):
      return self.facilities
    
available=(
   ('AVAILABLE','AVAILABLE'),
   ('NOT-AVAILABLE','NOT-AVAILABLE'),
)

# Create your models here.
class Rooms(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=200,blank=True)
    ammenities=models.ManyToManyField(Attributes,related_name='ammenities')
    location=models.ForeignKey(Location,on_delete=models.CASCADE) 
    address=models.TextField(max_length=500,blank=True)
    price=models.PositiveIntegerField(null = True)
    type=models.ForeignKey(Rcategory,on_delete=models.CASCADE) 
    availability=models.CharField(default="AVAILABLE",max_length=50,choices=available) 
    contact=models.IntegerField(blank=True,null = True)
    image=models.ImageField(blank=True,upload_to="room_images/") 
    info=models.TextField(blank=True) 
    created_date=models.DateTimeField(default=timezone.now) 


foodcategory=(
    ('lunch','lunch'),
    ('canteen','canteen'),
    ('restraunt','restraunt')
)

class Eatery(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.SET_NULL , null =True,blank=True)
    owner=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    category=models.CharField(max_length=50, choices=foodcategory)
    cuisine=models.CharField(max_length=200,blank=True)
    price=models.TextField(default="Write Your Price Here",blank=True)
    image=models.ImageField(blank=True,upload_to="food_images/")
    description=models.TextField()
    location=models.ForeignKey(Location,on_delete=models.CASCADE)
    address=models.CharField(max_length=100)
    contact=models.IntegerField(blank=True,null = True)
    created_date=models.DateTimeField(default=timezone.now)




    
    
    
