from django.urls import path,include
from . import views

# app_name = "myapp"
urlpatterns = [
    # path('', views.index),
    # path('excelupload', views.ExcelUploadView.as_view(), name='excel-upload'),
    path('', views.note_list, name='notepage'),
    path('create/', views.note_create ,name='create'),
    path('<int:pk>/update', views.note_update, name='update'),
    path('<int:pk>/delete', views.note_delete, name='delete'),
]