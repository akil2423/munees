from django.contrib import admin
from django.urls import path
from WeatherApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.home,name="Home"),
    path('fetch-weather/<str:name>',views.fetch_weather_and_forecast,name="fetch_weather_and_forecast")
    
]
