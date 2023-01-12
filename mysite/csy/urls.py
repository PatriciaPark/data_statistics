from django.urls import path
from . import views

app_name = "csy"
urlpatterns = [
    path('', views.index),
]