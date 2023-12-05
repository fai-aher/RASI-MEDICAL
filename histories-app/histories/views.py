import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core import serializers
from django.contrib import messages
from .models import HistoryEdit
from .forms import HistoryForm
from histories.serializers import HistorySerializer, HistoryEditSerializer, PrescriptionSerializer, LabResultSerializer
from patients.serializers import PatientSerializer
from patients.logic.logic_patients import get_patient_by_id
from histories.logic.logic_histories import get_history_by_patient_id, get_history_by_id, update_history

# Create your views here.

def patientHistories_view(request, patient_pk):
    patient = get_patient_by_id(patient_pk)
    history = get_history_by_patient_id(patient_pk)

    patient_serializer = PatientSerializer(patient)
    history_serializer = HistorySerializer(history)

    context = {
        'patient': patient_serializer.data,
        'history': history_serializer.data,
    }
    return render(request, 'Histories/patientHistories.html', context)


def history_edit(request, history_pk):
    history = get_history_by_id(history_pk)
    if request.method == 'POST':
        serializer = HistorySerializer(history, data=request.POST)
        if serializer.is_valid():
            serializer.save()

            # Create a new instance of HistoryEdit
            history_edit_data = serializer.data
            history_edit_data['history'] = history_pk
            history_edit_serializer = HistoryEditSerializer(data=history_edit_data)
            if history_edit_serializer.is_valid():
                history_edit_serializer.save()
                messages.add_message(request, messages.SUCCESS, 'Successfully updated history')
                return HttpResponseRedirect(reverse('edit_history', args=[history_pk]))
            else:
                print(history_edit_serializer.errors)
        else:
            print(serializer.errors)
    else:
        serializer = HistorySerializer(instance=history)

    context = {
        'form': serializer.data,
        'patient_id': history.patient_id,
    }
    return render(request, 'Histories/historyUpdate.html', context)


