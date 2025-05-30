from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm  # Your custom form

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # Redirect to tracker dashboard
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.POST.get('next', 'dashboard')  # Default to 'dashboard'
            return redirect(next_url)
    else:
        form = AuthenticationForm()
    
    # Provide default 'dashboard' if next is empty
    next_page = request.GET.get('next', 'dashboard')  # Changed from ''
    return render(request, 'accounts/login.html', {
        'form': form,
        'next': next_page
    })

def logout_view(request):
    logout(request)
    return redirect('login')