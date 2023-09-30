import json
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from patients.logic import logic_patients as patients_logic

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def patients_view(request):
    if request.method == 'GET':
        id_patient = request.GET.get('id', None)
        
        if id_patient:
            patient_dto = patients_logic.get_patient_by_id(id)
            patient = serializers.serialize('json', [patient_dto])
            return HttpResponse(patient, content_type='application/json')
        else:
            patients_dto = patients_logic.get_patients()
            patients = serializers.serialize('json', patients_dto)
            context = {
                'patient_list': patients
            }
            return render(request, 'Patient/patients.html', context)

    if request.method == 'POST':
        patient_dto = patients_logic.create_patient(json.loads(request.body))
        patient = serializers.serialize('json', [patient_dto])
        return HttpResponse(patient, content_type='application/json')


# Get a patient by ID

def patient_view(request, patient_pk):
    if request.method == 'GET':
        patient_dto = patients_logic.get_patient_by_id(patient_pk)
        patient = serializers.serialize('json', [patient_dto])
        return HttpResponse(patient, content_type='application/json')
    
    if request.method == 'PUT':
        patient_dto = patients_logic.update_patient(patient_pk, json.loads(request.body))
        patient = serializers.serialize('json', [patient_dto])
        return HttpResponse(patient, content_type='application/json')
    
    
