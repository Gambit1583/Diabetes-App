from django.urls import path
from .views import blood_sugar_tracker, food_diary, daily_diary, fetch_glucose_data

urlpatterns = [
    path('blood-sugar-tracker/', blood_sugar_tracker, name='blood_sugar_tracker'),
    path('food-diary/', food_diary, name='food_diary'),
    path('daily-diary/', daily_diary, name='daily_diary'),
    path('fetch_glucose_data/', fetch_glucose_data, name='fetch_glucose_data'),
]
