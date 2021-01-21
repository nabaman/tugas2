from django.shortcuts import render,HttpResponse
import requests

def dashboard_view(request):
    return render(request, 'dashboard.html')

def send_api2(request):
    loc_name = request.POST.get('loc_name')
    data = {
        'loc_name': loc_name
    }
    r = requests.post('http://localhost:8000/api/', data=data)
    print(r)
    return HttpResponse(r.json())