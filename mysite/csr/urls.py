from django.urls import path
from . import views

app_name = "csr"
urlpatterns = [
    path('', views.index),
]