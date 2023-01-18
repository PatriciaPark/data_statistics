from django.urls import path
from . import views

app_name = "store"
urlpatterns = [
    path('', views.index),
    path('update/', views.update, name='update'),
    path('select/', views.select, name='select'),
]