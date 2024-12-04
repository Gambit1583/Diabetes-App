import json
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import JsonResponse
from django.utils import timezone
from datetime import timedelta
from .models import BloodSugarRecord, FoodDiaryEntry, DailyDiaryEntry
from .forms import BloodSugarForm, FoodDiaryForm, DailyDiaryForm
import requests


@login_required
def blood_sugar_tracker(request):
    if request.method == "POST":
        form = BloodSugarForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.user = request.user
            record.save()
            return redirect('blood_sugars:blood_sugar_tracker')
    else:
        form = BloodSugarForm()

    # Define time ranges
    time_range = request.GET.get('time_range', '24h')
    time_ranges = {
        '24h': timedelta(hours=24),
        '48h': timedelta(hours=48),
        'weekly': timedelta(days=7),
        'monthly': timedelta(days=30),
        'quarterly': timedelta(days=90),
        'six_monthly': timedelta(days=180),
        'yearly': timedelta(days=365),
    }
    time_delta = time_ranges.get(time_range, timedelta(hours=24))

    # Fetch records
    now = timezone.now()
    records = BloodSugarRecord.objects.filter(user=request.user, date__gte=now - time_delta).order_by('-date')

    # Prepare data for chart
    labels = [record.date.strftime("%Y-%m-%d %H:%M:%S") for record in records]
    data = [record.blood_sugar_level for record in records]

    context = {
        'form': form,
        'records': records,
        'labels': json.dumps(labels),  # Serialize labels to JSON
        'data': json.dumps(data),      # Serialize data to JSON
        'time_range': time_range       # Pass current time range selection to template
    }

    return render(request, 'blood_sugars/blood_sugar_tracker.html', context)


@login_required
def food_diary(request):
    if request.method == 'POST':
        form = FoodDiaryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect('blood_sugars:food_diary')
    else:
        form = FoodDiaryForm()

    # Fetch all diary entries for the user
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
            return redirect('blood_sugars:daily_diary')
    else:
        form = DailyDiaryForm()

    # Fetch all diary entries for the user
    entries = DailyDiaryEntry.objects.filter(user=request.user).order_by('-entry_time')

    return render(request, 'blood_sugars/daily_diary.html', {'form': form, 'entries': entries})


@login_required
def fetch_glucose_data(request):
    user = request.user  # Get the current authenticated user

    # Define the API endpoint and headers
    api_url = 'https://api.freestylelibre.com/v1/glucose'
    headers = {
        'Authorization': f'Bearer {settings.FREESTYLE_LIBRE_API_KEY}',
        'Content-Type': 'application/json',
    }

    try:
        # Make the API request
        response = requests.get(api_url, headers=headers, params={'user_id': user.id})
        response.raise_for_status()

        # Process the API response
        data = response.json()
        for record in data.get('records', []):  # Safely handle missing 'records'
            BloodSugarRecord.objects.create(
                user=user,
                date=record.get('timestamp', timezone.now()),  # Use current time if timestamp is missing
                blood_sugar_level=record.get('glucose', 0),  # Default to 0 if glucose is missing
                carbohydrates_eaten=record.get('carbs', 0)  # Default to 0 carbs if missing
            )
        return JsonResponse({'status': 'success'}, status=200)

    except requests.exceptions.RequestException as e:
        # Log or handle the error appropriately
        return JsonResponse({'error': str(e)}, status=500)

    except json.JSONDecodeError:
        return JsonResponse({'error': 'Failed to parse API response'}, status=500)
