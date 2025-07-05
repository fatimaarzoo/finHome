from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields=['username','password1','password2']

    def save(self,commit=True):
        user = super().save(commit=False)
        user.role = 'student'
        if commit:
            user.save()
        return user

class RenterRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username','password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'renter'
        if commit:
            user.save()
        return user

class SellerRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username','password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'seller'
        if commit:
            user.save()
        return user
    
class StudentUpdateProfile(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    uni = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model= UserProfile
        fields=['uni','image']

class RenterUpdateProfile(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    building = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model=RenterProfile
        fields=['building','image']

class SellerUpdateProfile(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    service = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model=SellerProfile
        fields=['service','image']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=CustomUser
        fields=['username','email']
