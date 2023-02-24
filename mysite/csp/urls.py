from django.urls import path
from . import views

app_name = "csp"
urlpatterns = [
    path('', views.index),
    path('select/', views.select, name='select'),
    path('select2/', views.select2, name='select2'),
]