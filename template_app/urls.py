from django.urls import path
from . import views

#app_name register, {% url app_name:view %}
app_name = "template_app"

urlpatterns = [
    path("",views.index,name="index"),
    path("weather/",views.weather_view,name="weatherview")
]
