from django.db import models
from django.contrib.auth.models import User
from datetime import time

def default_meal_time():
    return time(6, 30)

class BloodSugarRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    blood_sugar_level = models.FloatField()
    carbohydrates_eaten = models.FloatField()
    bolus_insulin = models.FloatField(blank=True, null=True)
    basal_insulin = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}: {self.blood_sugar_level} mg/dL on {self.date}"

class FoodDiaryEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meal_time = models.TimeField(default=default_meal_time)
    food_item = models.CharField(max_length=200)
    calories = models.IntegerField()

    def __str__(self):
        return f"{self.food_item} for {self.user.username} at {self.meal_time}"

class DailyDiaryEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    entry_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return f"Diary entry for {self.user.username} on {self.entry_time}"
