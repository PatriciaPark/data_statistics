from django.urls import path
from . import views

app_name = "sqldown"
urlpatterns = [
    path('', views.index, name = 'main'),
]