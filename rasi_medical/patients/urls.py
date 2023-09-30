from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('', views.patients_view, name='view_patients'),
    path('<int:patient_pk>', views.patient_view, name='view_patient'),
    path('patientcreate/', csrf_exempt(views.patient_create), name='patientCreate'),
]