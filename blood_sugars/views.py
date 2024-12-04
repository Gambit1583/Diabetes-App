from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import BloodSugarRecord, FoodDiaryEntry, DailyDiaryEntry
from .forms import BloodSugarForm, FoodDiaryForm, DailyDiaryForm
import requests
from django.conf import settings
from django.http import JsonResponse

@login_required
def blood_sugar_tracker(request):
    if request.method == "POST":
        form = BloodSugarForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.user = request.user
            record.save()
            return redirect('blood_sugar_tracker')
    else:
        form = BloodSugarForm()
    records = BloodSugarRecord.objects.filter(user=request.user).order_by('-date')
    return render(request, 'blood_sugars/blood_sugar_tracker.html', {'form': form, 'records': records})

@login_required
def food_diary(request):
    if request.method == 'POST':
        form = FoodDiaryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect('food_diary')
    else:
        form = FoodDiaryForm()
    entries = FoodDiaryEntry.objects.filter(user=request.user).order_by('-meal_time')
    return render(request, 'blood_sugars/food_diary.html', {'form': form, 'entries': entries})

@login_required
def daily_diary(request):
    if request.method == 'POST':
        form = DailyDiaryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect('daily_diary')
    else:
        form = DailyDiaryForm()
    entries = DailyDiaryEntry.objects.filter(user=request.user).order_by('-entry_time')
    return render(request, 'blood_sugars/daily_diary.html', {'form': form, 'entries': entries})

@login_required
def fetch_glucose_data(request):
    user = request.user  # This retrieves the current authenticated user

    # Define the API endpoint and headers
    api_url = 'https://api.freestylelibre.com/v1/glucose'
    headers = {
        'Authorization': f'Bearer {settings.FREESTYLE_LIBRE_API_KEY}',
        'Content-Type': 'application/json',
    }

    # Make the API request
    response = requests.get(api_url, headers=headers, params={'user_id': user.id})

    # Handle the API response
    if response.status_code == 200:
        data = response.json()
        for record in data['records']:
            BloodSugarRecord.objects.create(
                user=user,
                date=record['timestamp'],
                blood_sugar_level=record['glucose'],
                carbohydrates_eaten=record.get('carbs', 0)
            )
        return JsonResponse({'status': 'success'}, status=200)
    else:
        # Handle errors
        return JsonResponse({'error': response.text}, status=response.status_code)


