from django.shortcuts import render
from dotenv import load_dotenv
import requests
import os

load_dotenv()

BASE_URL = os.getenv('BASE_URL')
API_KEY = os.getenv('API_KEY')

def weather(request):
    if request.method == 'POST':
        city = request.POST['city']
        weather = BASE_URL + city + '&appid=' + API_KEY
        weather_request =  requests.get(weather).json()    
        
        context = {
            'title' : 'openweather',
            'data' : weather_request,
        }
        return render(request, 'weather/index.html', {'context' : context})
    else:
        return render(request, 'weather/index.html')
   
