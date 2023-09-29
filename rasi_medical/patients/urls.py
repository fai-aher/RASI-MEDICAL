from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.patients_view, name='view_patients'),
    path('<int:patient_pk>', views.patient_view, name='view_patient'),
]