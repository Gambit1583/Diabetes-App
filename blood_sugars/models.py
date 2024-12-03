from django.db import models
from django.contrib.auth.models import User

class BloodSugarRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    blood_sugar_level = models.FloatField()
    carbohydrates_eaten = models.FloatField()

    def __str__(self):
        return f"Record for {self.user.username} on {self.date}"

class FoodDiaryEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meal_time = models.DateTimeField
    food_item = models.CharField(max_length=200)
    calories = models.IntegerField()

    def __str__(self):
        return f"{self.food_item} at {self.meal_time}"

class DailyDiaryEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    entry_time = models.DateTimeField(auto_now_add=True)
    content =models.TextField()

    def __str__(self):
        return f"Entry for {self.user.username} on {self.entry_time}"
