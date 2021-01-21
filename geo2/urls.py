from django.contrib import admin
from django.urls import path,include
from .views import dashboard_view,send_api2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-2/',include('api.urls')),
    path('',dashboard_view),
    path('send-api-2/',send_api2)
]
