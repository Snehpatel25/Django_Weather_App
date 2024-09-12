from django.shortcuts import render
import requests
from django.conf import settings  # To get API key from settings
from .forms import CityForm

def weather_view(request):
    # API URL pattern (with proper placeholders for city and API key)
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}'
    
    # Retrieve API key from Django settings (add this in your settings.py)
    api_key = settings.OPENWEATHERMAP_API_KEY
    
    # Default city if none is provided by the form
    city = 'New York'
    error_message = None

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
    else:
        form = CityForm()

    try:
        # Make a request to OpenWeatherMap API with the city and API key
        response = requests.get(url.format(city, api_key)).json()
        
        if response.get('cod') != 200:
            # If there's an error in the response (like an invalid city or server issue)
            error_message = response.get('message', 'Error fetching data from OpenWeatherMap API')
            weather = None
        else:
            # Extract and prepare the weather information to pass to the template
            weather = {
                'city': city,
                'temperature': round(response['main']['temp']),
                'description': response['weather'][0]['description'],
                'icon': response['weather'][0]['icon'],
            }
    except requests.exceptions.RequestException as e:
        # If there's an exception while making the request (network issue, etc.)
        error_message = str(e)
        weather = None

    # Prepare context to pass to the template
    context = {
        'weather': weather, 
        'form': form, 
        'error_message': error_message
    }

    return render(request, 'weather/weather.html', context)
