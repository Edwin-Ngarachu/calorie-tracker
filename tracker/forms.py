from django import forms
from .models import Food, FoodLog

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'calories']

class FoodLogForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['food'].queryset = Food.objects.filter(created_by=user)
    
    class Meta:
        model = FoodLog
        fields = ['food', 'quantity']
        widgets = {
            'quantity': forms.NumberInput(attrs={'min': 1})
        }