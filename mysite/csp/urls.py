from django.urls import path
from . import views

app_name = "csp"
urlpatterns = [
    path('', views.index),
]