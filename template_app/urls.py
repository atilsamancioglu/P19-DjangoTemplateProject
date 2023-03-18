from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("weather/",views.weather_view,name="weatherview")
]