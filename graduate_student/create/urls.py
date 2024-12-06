from django.urls import path
from . import views
from .views import upload_csv

urlpatterns = [
    path('', views.create_choice, name='create_choice'),
    path('student_form', views.student_create, name='student_create'),
    path('history_form', views.history_create, name='history_create'),
    path('company_form', views.company_create, name='company_create'),
    path('upload-csv', views.upload_csv, name='upload_csv'),
    path('upload-csv/success-url', views.success_url, name='success'),
    path('upload-csv/error', views.error_url, name='error')
]