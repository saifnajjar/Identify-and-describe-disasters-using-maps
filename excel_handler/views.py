from django.shortcuts import render
from .models import Hurricane, Earthquake

def index(request):
    return render(request, 'excel_handler/index.html')

def disasters(request):
    hurricanes = Hurricane.objects.all()
    earthquakes = Earthquake.objects.all()
    return render(request, 'excel_handler/disasters.html', {'hurricanes': hurricanes, 'earthquakes': earthquakes})