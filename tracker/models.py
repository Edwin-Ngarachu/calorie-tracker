from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class Food(models.Model):
    name = models.CharField(max_length=200)
    calories = models.PositiveIntegerField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class FoodLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_calories(self):
        return self.food.calories * self.quantity

    def __str__(self):
        return f"{self.user.username} - {self.food.name} ({self.date})"