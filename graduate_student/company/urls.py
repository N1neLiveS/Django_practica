from django.urls import path
from . import views

urlpatterns = [
    path('', views.company_storage, name='company'),
    path('<int:pk>', views.CompanyDetailView.as_view(), name='company-detail')
]