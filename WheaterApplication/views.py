from django.shortcuts import render
from django.contrib import messages
import requests
import datetime

# Create your views here.
def home(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Bengaluru'

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=2bc3469bedfda9b60492d79e3c3331ad'
    PARAMS = {'units': 'metric'}
    
    try:
        data = requests.get(url, PARAMS).json()
        # print(data)
        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']
        day = datetime.date.today()

        return render(request,'index.html',{'description':description,'icon':icon,'temp':temp,'day':day,'city':city,'exception_occured':False})
    except:
        exception_occured = True
        messages.error(request,'Enter Data is not Available')
        day = datetime.date.today()
        return render(request,'index.html',{'description':'clear sky','icon':'01d','temp':25,'day':day,'city':'Bengalore', 'exception_occured':exception_occured})