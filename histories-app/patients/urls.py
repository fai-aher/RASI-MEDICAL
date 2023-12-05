from django.contrib import admin
from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt
from . import views
from histories import views as histories_views

urlpatterns = [
    path('', views.patients_view, name='view_patients'),
    path('<int:patient_pk>', views.patient_view, name='view_patient'),
    path('patientcreate/', csrf_exempt(views.patient_create), name='patientCreate'),
    path('<int:patient_pk>/histories', histories_views.patientHistories_view, name='patientHistories'),
]