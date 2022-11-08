from django.urls import path,include
from . import views

# app_name = "myapp"
urlpatterns = [
    path('', views.list),
    path('excelupload/', views.post, name='excel-upload'),
]