from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from .forms import *
from rental.forms import *
from rental.models import *
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,PasswordChangeView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import DeleteView
import os
from dotenv import load_dotenv
import json
import requests

# Create your views here.
def register_student(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('dashboard')
    else:
        form= UserRegisterForm()
    return render(request,'accounts/register.html',{'form':form,'role':'student'})

def register_renter(request):
    if request.method=='POST':
        form=RenterRegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('dashboard')
    else:
        form=RenterRegisterForm()
    return render(request,'accounts/register.html',{'form':form,'role':'renter'})

def register_seller(request):
    if request.method=='POST':
        form=SellerRegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            print('Your account has been created')
            login(request,user)
            return redirect('dashboard')
    else:
        form=SellerRegisterForm()
    return render(request,'accounts/register.html',{'form':form, 'role':'seller'})

class UserLoginView(LoginView):
    template_name = 'accounts/login.html'

    def get_success_url(self):
        user = self.request.user
        if user.role == 'student':
            return reverse_lazy('dashboard')
        elif user.role == 'renter':
            return reverse_lazy('dashboard')
        elif user.role == 'seller':
            return reverse_lazy('dashboard')
        return reverse_lazy('home')
    
@login_required
def logout_page(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    user=request.user
    room_list=Rooms.objects.all().filter(user=user)
    food_list=Eatery.objects.all().filter(user=user)
    user=request.user

    context={
        'user':user,
        'roomlist':room_list,
        'foodlist':food_list,
        'user':user,
    }
    return render(request,'accounts/dashboard.html',context)

@login_required
def stdprofile(request):
    if request.method=='POST':
        p_form=StudentUpdateProfile(request.POST, request.FILES, instance=request.user.userprofile)
        if  p_form.is_valid():
            p_form.save()
            print('profile of student made')
            messages.success(request, 'Your profile is updated successfully')
            return redirect('profile_student')
    else:
        p_form = StudentUpdateProfile(instance=request.user.userprofile)

    return render(request, 'accounts/profile.html',{'p_form':p_form})

@login_required
def rntprofile(request):
    if request.method=='POST':
        p_form=RenterUpdateProfile(request.POST, request.FILES, instance=request.user.renterprofile)
        if  p_form.is_valid():
            p_form.save()
            print('profile of tenent made')
            messages.success(request, 'Your profile is updated successfully')
            return redirect('profile_renter')
    else:
        p_form = RenterUpdateProfile(instance=request.user.renterprofile)
        
    return render(request, 'accounts/profile.html',{'p_form':p_form})

@login_required
def slrprofile(request):
    if request.method=='POST':
        p_form=SellerUpdateProfile(request.POST, request.FILES, instance=request.user.sellerprofile)
        if  p_form.is_valid():
            p_form.save()
            print('profile of seller made')
            messages.success(request, 'Your profile is updated successfully')
            return redirect('profile_seller')
    else:
        p_form = SellerUpdateProfile(instance=request.user.sellerprofile)
        

    return render(request, 'accounts/profile.html',{'p_form':p_form})


class ChangePasswordView(SuccessMessageMixin,PasswordChangeView):
    template_name='accounts/change_password.html'
    success_message='Your password is changed successfully'
    success_url=reverse_lazy('profile')

@login_required
def user_update(request):
    if request.method=='POST':
        u_form=UserUpdateForm(request.POST,request.FILES,instance=request.user)
        if  u_form.is_valid():
            u_form.save()
            messages.success(request, 'Your userid is updated successfully')
            return redirect('dashboard')
    else:
        u_form= UserUpdateForm(instance=request.user)

    return render(request, 'accounts/user_update.html',{'u_form':u_form})


class UserDeleteView(DeleteView):
    model =CustomUser
    template_name="accounts/user_delete.html"
    success_url=('/')
    

def choose_register(request):
    return render(request,'accounts/choose_register.html')


load_dotenv()
w_api = os.getenv("OPEN_WEATHER_API_KEY")

def check_weather(request):
    CITY = 'Lucknow'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={w_api}&units=metric'

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
       temp = data['main']['temp']
       description = data['weather'][0]['description']
       icon= data['weather'][0]['icon']
       return HttpResponse(f"Weather in {CITY}: {temp}°C, {description}, {icon}")
    else:
       return HttpResponse(f"Error: {data.get('message', 'Something went wrong.')}")
   