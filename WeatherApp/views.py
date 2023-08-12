from django.shortcuts import render,redirect
from .form import CityForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from django.contrib import messages

# Create your views here.

# def home(request):

@api_view(['GET'])
def fetch_weather_and_forecast(request,name):
    print(request,"request....")
    print(name,"name....")
    # print(request.ge,"request.....")
    # city="chennai"
    api_key = "f423f2aa64f2650df74dc243f3b5e359"
    # url='https://api.openweathermap.org/data/2.5/weather?q=CHENNAI&appid=f423f2aa64f2650df74dc243f3b5e359&units=metric'
    url='http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'

    # response = requests.get(url).json()
    response = requests.get(url.format(name,api_key)).json()
    print(response,"response..................")
    # weather={
    #     "main": response["main"],
    #     "location": response["name"]
    # }

    # print(weather,"weatherweatherweatherweather...")
  
    return Response(response)
