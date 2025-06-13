from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Search
from .forms import SearchForm
import folium
import geocoder

# Create your views here.

def map(request, address):

    print(f"{address = }")
    headers = {"User-Agent": "CrimeReport/1.0 (mrunal.narayana@gmail.com)"}
    location = geocoder.get(address, provider='osm', headers=headers)
    print(f"{location = }")
    lat = location.lat
    lng = location.lng
    country = location.country
    if lat == None or lng == None or address == None:
        return HttpResponse('You address input is invalid')
    # Create Map Object
    m = folium.Map(location=[19, -12], zoom_start=2)
    folium.Marker([lat, lng], tooltip='Click for more', popup=country).add_to(m)
    # Get HTML Representation of Map Object
    return render(request, 'location/maps.html', {"m": m._repr_html_()})

def search(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        return redirect('map', address=address)
    return render(request, 'location/search.html', {"form": SearchForm()})