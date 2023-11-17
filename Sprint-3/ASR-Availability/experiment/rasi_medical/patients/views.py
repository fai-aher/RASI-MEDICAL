import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core import serializers
from django.contrib import messages
from .forms import PatientForm
from patients.logic import logic_patients as patients_logic

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from rasi_medical.auth0backend import getRole

@csrf_exempt
@login_required
def patients_view(request):
    if request.method == 'GET':
        id_patient = request.GET.get('id', None)
        
        if id_patient:
            patient_dto = patients_logic.get_patient_by_id(id)
            patient = serializers.serialize('json', [patient_dto])
            return HttpResponse(patient, content_type='application/json')
        else:
            patients = patients_logic.get_patients()
            context = {
                'patient_list': patients
            }
            return render(request, 'Patient/patients.html', context)

    if request.method == 'POST':
        patient_dto = patients_logic.create_patient(json.loads(request.body))
        patient = serializers.serialize('json', [patient_dto])
        return HttpResponse(patient, content_type='application/json')


# Get a patient by ID

@login_required
def patient_view(request, patient_pk):
    if request.method == 'GET' and getRole(request) == 'medico':
        patient_dto = patients_logic.get_patient_by_id(patient_pk)
        patient = serializers.serialize('json', [patient_dto])
        return HttpResponse(patient, content_type='application/json')
    
    if request.method == 'PUT' and getRole(request) == 'medico':
        patient_dto = patients_logic.update_patient(patient_pk, json.loads(request.body))
        patient = serializers.serialize('json', [patient_dto])
        return HttpResponse(patient, content_type='application/json')
    
    

def patient_create(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patients_logic.create_patient(form)
            messages.add_message(request, messages.SUCCESS, 'Successfully created patient')
            return HttpResponseRedirect(reverse('patientCreate'))
        else:
            print(form.errors)
    else:
        form = PatientForm()

    context = {
        'form': form,
    }
    return render(request, 'Patient/patientCreate.html', context)

