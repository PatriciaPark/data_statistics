from django.urls import path
from . import views

app_name = "csd"
urlpatterns = [
    path('', views.index),
    path('upload/', views.upload, name='upload'),
]