from django.urls import path,include
from . import views

# app_name = "myapp"
urlpatterns = [
    # path('', views.list),
    # path('excelupload/', views.post, name='excel-upload'),
    path('daily/', views.dailyToDB, name='daily_to_db'),
    path('monthly/', views.monthlyToDB, name='monthly_to_db'),
    path('yearly/', views.yearlyToDB, name='yearly_to_db'),
    path('store/', views.storeInfoToDB, name='storeinfo_to_db'),
    # path('fileView/', views.fileView, name='upload_fileView'),
    path('file/', views.uploadFile, name='upload_file'),
    path('', views.fileView, name='upload_fileView'),
    # path('', views.loginView, name='main_loginView'),
    path('index/', views.index, name='main_index'),
]