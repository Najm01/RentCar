from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistrationForm, LoginForm, CarForm
from .models import User, Car

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            auth_login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('home')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username_or_email = form.cleaned_data['username_or_email']
            password = form.cleaned_data['password']
            user = User.objects.filter(username=username_or_email).first() or \
                   User.objects.filter(email=username_or_email).first()

            if user and user.check_password(password):
                auth_login(request, user)
                messages.success(request, f"Welcome back, {user.username}!")
                return redirect('home')
            else:
                messages.error(request, "Invalid username/email or password.")
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

@login_required
def home(request):
    # Get all cars in addition to the logged-in user's cars
    cars = Car.objects.all()  # This fetches all cars
    user_cars = Car.objects.filter(user=request.user)  # This fetches the user's cars
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            car = form.save(commit=False)
            car.user = request.user
            car.save()
            messages.success(request, "Car added successfully!")
            return redirect('home')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CarForm()
    return render(request, 'users/home.html', {'cars': cars, 'user_cars': user_cars, 'form': form})

@login_required
def car_list(request):
    cars = Car.objects.filter(user=request.user)  # Filter cars by logged-in user
    return render(request, 'users/car_list.html', {'cars': cars})

@login_required
def delete_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if car.user == request.user:
        car.delete()
        messages.success(request, "Car deleted successfully!")
    else:
        messages.error(request, "You are not authorized to delete this car.")
    
    cars = Car.objects.filter(user=request.user)
    return render(request, 'users/home.html', {'cars': cars})

def logout_view(request):
    logout(request)
    return redirect('login')

