from django.urls import path
from . import views

app_name = "csm"
urlpatterns = [
    path('', views.index),
    path('upload/', views.upload, name='upload'),
    path('select/', views.select, name='select'),
    path('select2/', views.select2, name='select2'),
]