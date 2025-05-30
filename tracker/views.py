from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Food, FoodLog
from .forms import FoodForm, FoodLogForm


@login_required
def food_list(request):
    foods = Food.objects.filter(created_by=request.user)
    return render(request, 'tracker/food_list.html', {'foods': foods})

@login_required
def dashboard(request):
    today = timezone.now().date()
    food_logs = FoodLog.objects.filter(user=request.user, date=today)
    total_calories = sum(log.total_calories for log in food_logs)
    user_goal = request.user.daily_calorie_goal
    remaining_calories = max(0, user_goal - total_calories)

    context = {
        'food_logs': food_logs,
        'total_calories': total_calories,
        'user_goal': user_goal,
        'remaining_calories': remaining_calories,
        'date': today
    }
    return render(request, 'tracker/dashboard.html', context)

@login_required
def add_food(request):
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            food = form.save(commit=False)
            food.created_by = request.user
            food.save()
            return redirect('food_list')  # Or 'dashboard' if you prefer
        # If form is invalid, we'll continue to render the form with errors
    else:
        form = FoodForm()
    
    # This return statement must be outside the if/else blocks
    return render(request, 'tracker/add_food.html', {'form': form})
@login_required
def log_food(request):
    if request.method == 'POST':
        form = FoodLogForm(request.POST, user=request.user)
        if form.is_valid():
            food_log = form.save(commit=False)
            food_log.user = request.user
            food_log.save()
            return redirect('dashboard')
    else:
        form = FoodLogForm(user=request.user)
    return render(request, 'tracker/log_food.html', {'form': form})

@login_required
def delete_food_log(request, log_id):
    food_log = get_object_or_404(FoodLog, id=log_id, user=request.user)
    if request.method == 'POST':
        food_log.delete()
    return redirect('dashboard')

@login_required
def reset_day(request):
    today = timezone.now().date()
    FoodLog.objects.filter(user=request.user, date=today).delete()
    return redirect('dashboard')