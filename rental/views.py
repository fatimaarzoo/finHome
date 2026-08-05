from django.shortcuts import render, get_object_or_404, redirect
from rental.models import *
from rental.forms import *
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView
from django.db.models import Q
from django.contrib import messages

def home(request):
    user = request.user
    context = {
        'rooms': Rooms.objects.all(),
        'user': user
    }
    return render(request, 'rental/home.html', context)

def contact(request):
    return render(request, 'rental/contact.html')

def about(request):
    return render(request, 'rental/about.html')

def house(request):
    user = request.user
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    

    try:
        if request.GET.get('search'):
            sdata = request.GET.get('search')
            room = Rooms.objects.filter(
                Q(location__area__icontains=sdata) |
                Q(name__icontains=sdata)
            )
        else:
            room = Rooms.objects.all()

        if min_price:
            room = room.filter(price__gte=min_price)
        if max_price:
            room = room.filter(price__lte=max_price)

    except Exception as e:
        messages.error(request, f"Error fetching room data: {e}")
        room = Rooms.objects.none()

    context = {
        'rooms': room,
    }
    return render(request, 'rental/house.html', context)

def food(request):
    user = request.user
    fcategory = request.GET.get('category')

    try:
        if request.GET.get('search'):
            sdata = request.GET.get('search')
            food = Eatery.objects.filter(
                Q(name__icontains=sdata) |
                Q(location__area__icontains=sdata)
            )
        else:
            food = Eatery.objects.all()

        if fcategory and fcategory != 'ALL':
            food = food.filter(category=fcategory)

    except Exception as e:
        messages.error(request, f"Error loading food services: {e}")
        food = Eatery.objects.none()

    context = {
        'foods': food,
    }
    return render(request, 'rental/food.html', context)

def detail(request, id):
    room = get_object_or_404(Rooms, id=id)
    return render(request, 'rental/detail.html', {'room': room})

def fdetail(request, id):
    food = get_object_or_404(Eatery, id=id)
    return render(request, 'rental/fdetail.html', {'food': food})

def addroom(request):
    form = Addrooms(request.POST ,request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            try:
                r = form.save(commit=False)
                r.user = request.user
                r.save()
                messages.success(request, "Room added successfully.")
                return redirect('room')
            except Exception as e:
                messages.error(request, f"Error saving room: {e}")
    return render(request, 'rental/addrooms.html', {'forms': form})

def addfood(request):
    form = Addeatery(request.POST or None,request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            try:
                r = form.save(commit=False)
                r.user = request.user
                r.save()
                messages.success(request, "Eatery added successfully.")
                return redirect('food')
            except Exception as e:
                messages.error(request, f"Error saving eatery: {e}")
    return render(request, 'rental/addeatery.html', {'form': form})

def update_room(request, id):
    room = get_object_or_404(Rooms, id=id)
    form = Addrooms(request.POST or None,request.FILES or None, instance=room)
    if form.is_valid():
        try:
            form.save()
            messages.success(request, "Room updated successfully.")
            return redirect('detail', id=id)
        except Exception as e:
            messages.error(request, f"Error updating room: {e}")
    return render(request, 'rental/update_room.html', {'form': form})

def delete_room(request, id):
    try:
        room = get_object_or_404(Rooms, id=id)
        room.delete()
        messages.success(request, "Room deleted successfully.")
    except Exception as e:
        messages.error(request, f"Error deleting room: {e}")
    return redirect('/')

def update_food(request, id):
    food = get_object_or_404(Eatery, id=id)
    form = Addeatery(request.POST or None,request.FILES or None,  instance=food)
    if form.is_valid():
        try:
            form.save()
            messages.success(request, "Eatery updated successfully.")
            return redirect('fdetail', id=id)
        except Exception as e:
            messages.error(request, f"Error updating eatery: {e}")
    return render(request, 'rental/update_food.html', {'form': form})

def delete_food(request, id):
    try:
        food = get_object_or_404(Eatery, id=id)
        food.delete()
        messages.success(request, "Eatery deleted successfully.")
    except Exception as e:
        messages.error(request, f"Error deleting eatery: {e}")
    return redirect('/')
