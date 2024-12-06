from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_storage, name='students'),
    path('<int:pk>', views.PersonDetailView.as_view(), name='person-detail'),
    path('<int:pk>/personal/', views.personal_details, name='personal_details'),
    path('<int:pk>/personal/pdf/', views.export_to_pdf, name='export_personal_pdf'),
    path('<int:pk>/employment/', views.employment_details, name='employment_details')
]