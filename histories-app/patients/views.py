import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core import serializers
from django.contrib import messages
from .forms import PatientForm
from patients.logic import logic_patients as patients_logic
from django.views.decorators.csrf import csrf_exempt
from histories.serializers import HistorySerializer, HistoryEditSerializer, PrescriptionSerializer, LabResultSerializer
from patients.serializers import PatientSerializer
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import status

from django.views.decorators.csrf import csrf_exempt


def patients_view(request):
    if request.method == 'GET':
        id_patient = request.GET.get('id', None)
            
        if id_patient:
            patient_dto = patients_logic.get_patient_by_id(id_patient)
            serializer = PatientSerializer(patient_dto)
            patient = serializers.serialize('json', [patient_dto])
            return HttpResponse(patient, content_type='application/json')
        else:
            patients = patients_logic.get_patients()
            serializer = PatientSerializer(patients, many=True)
            context = {
                'patient_list': serializer.data
            }
            return render(request, 'Patient/patients.html', context)

    if request.method == 'POST':
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            patient_dto = patients_logic.create_patient(serializer.validated_data)
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse(status=401)


# Get a patient by ID

def patient_view(request, patient_pk):
    if request.method == 'GET':
        patient_dto = patients_logic.get_patient_by_id(patient_pk)
        serializer = PatientSerializer(patient_dto)
        patient = serializers.serialize('json', [patient_dto])
        return HttpResponse(patient, content_type='application/json')
    
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PatientSerializer(data=data)
        if serializer.is_valid():
            patient_dto = patients_logic.update_patient(patient_pk, serializer.validated_data)
            return HttpResponse(patient, content_type='application/json')
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

def patient_create(request):
    if request.method == 'POST':
        serializer = PatientSerializer(data=request.POST)
        if serializer.is_valid():
            patients_logic.create_patient(serializer)
            messages.add_message(request, messages.SUCCESS, 'Successfully created patient')
            return HttpResponseRedirect(reverse('patientCreate'))
        else:
            print(serializer.errors)    
    serializer = PatientSerializer()
    context = {
        'form': serializer.data,
    }
    return render(request, 'Patient/patientCreate.html', context)

