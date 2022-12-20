from django.urls import path,include
from . import views

app_name = "csp"
urlpatterns = [
    path('', views.index),
]