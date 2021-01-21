from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from geopy import Nominatim

@api_view(['POST'])
def get_api(request):
    lat = request.data.get('lat')
    long = request.data.get('long')
    if lat == '' or long == '':
        return Response('error', status=400)
    geolocator = Nominatim(user_agent="myAgent")
    location = geolocator.reverse(f'{lat}/{long}', timeout=None, zoom=18)
    loc_geo = geolocator.geocode(location.address, timeout=None)
    importance = float(loc_geo.raw['importance'])
    warna = 'merah' if importance >= 0 and importance <= 1 else 'kuning' if importance > 1 and importance <= 2 else 'hijau'

    return Response(f'{location.address} , {warna}', status=200)