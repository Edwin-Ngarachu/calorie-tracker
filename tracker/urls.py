from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add-food/', views.add_food, name='add_food'),
    path('food-list/', views.food_list, name='food_list'),
    path('log-food/', views.log_food, name='log_food'),
    path('delete-log/<int:log_id>/', views.delete_food_log, name='delete_food_log'),
    path('reset-day/', views.reset_day, name='reset_day'),
]