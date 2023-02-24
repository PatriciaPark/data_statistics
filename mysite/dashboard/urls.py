from django.urls import path
from . import views

app_name = "dashboard"
urlpatterns = [
    path('', views.index, name = 'main'),
    path('create_price', views.create_price, name = 'create_price'),
    path('create_month', views.create_month, name = 'create_month'),
    path('twmap/', views.twmap, name = 'taiwan_map'),
]