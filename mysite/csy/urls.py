from django.urls import path
from . import views

app_name = "csy"
urlpatterns = [
    path('', views.index),
    path('detail/', views.detail, name='detail'),
    path('select/', views.select, name='select'),
    path('select2/', views.select2, name='select2'),
]