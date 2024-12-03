from django import forms
from .models import BloodSugarRecord, FoodDiaryEntry, DailyDiaryEntry

class BloodSugarForm(forms.ModelForm):
    class Meta:
        model = BloodSugarRecord
        fields = ['blood_sugar_level', 'carbohydrates_eaten']

class FoodDiaryForm(form.ModelForm):
    class Meta:
        model = FoodDiaryEntry
        fields = ['meal_time', 'food_item', 'calories']

class DailyDiaryForm(forms.ModelForm):
    class Meta:
        model = DailyDiaryEntry
        fields = ['content']