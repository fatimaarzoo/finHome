from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import *

@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created and instance.role=='student':
        UserProfile.objects.create(user=instance)
    elif created and instance.role=='renter':
        RenterProfile.objects.create(user=instance)
    elif created and instance.role=='seller':
        SellerProfile.objects.create(user=instance)


@receiver(post_save, sender=CustomUser)
def save_profile(sender, instance, **kwargs):
    if instance.role=='student':
       instance.userprofile.save()
    elif instance.role=='renter':
        instance.renterprofile.save()
    elif instance.role=='seller':
        instance.sellerprofile.save()