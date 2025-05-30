from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    daily_calorie_goal = models.PositiveIntegerField(default=2000)
    
    # Add this to avoid clashes in future migrations
    class Meta:
        db_table = 'custom_user'