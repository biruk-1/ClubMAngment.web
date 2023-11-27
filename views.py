from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User  # Add this import
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Event
from .forms import CreateUserForm, EventForm

def home(request):
    return render(request, 'club/home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'club/login.html')

def logout_view(request):
    logout(request)
    return redirect('club:home')

def member_add(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Member added successfully.')
            return redirect('home')
        else:
            messages.error(request, 'Error adding member. Please check the form.')
    else:
        form = CreateUserForm()
    
    return render(request, 'club/member_add.html', {'form': form})

@login_required
def event_list(request):
    events = Event.objects.all()
    return render(request, 'club/event_list.html', {'events': events})

@login_required
def event_add(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save()
            messages.success(request, 'Event added successfully.')
            return redirect('event_list')
        else:
            messages.error(request, 'Error adding event. Please check the form.')
    else:
        form = EventForm()
    
    return render(request, 'club/event_add.html', {'form': form})

@login_required
def event_detail(request, event_id):
    try:
        event = Event.objects.get(id=event_id)
        return render(request, 'club/event_detail.html', {'event': event})
    except Event.DoesNotExist:
        messages.error(request, 'Event not found.')
        return redirect('club:event_list')
@login_required
def member_delete(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    messages.success(request, 'User deleted successfully.')
    return redirect('home')

@login_required
def event_delete(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.delete()
    messages.success(request, 'Event deleted successfully.')
    return redirect('event_list')