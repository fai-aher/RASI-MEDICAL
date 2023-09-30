import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core import serializers
from django.contrib import messages
from .forms import HistoryForm
from patients.logic.logic_patients import get_patient_by_id
from histories.logic.logic_histories import get_history_by_patient_id, get_history_by_id, update_history

# Create your views here.

def patientHistories_view(request, patient_pk):
    context = {
        'patient': get_patient_by_id(patient_pk),
        'history': get_history_by_patient_id(patient_pk),
    }
    return render(request, 'Histories/patientHistories.html', context)


def history_edit(request, history_pk):
    history = get_history_by_id(history_pk)
    patient_id = history.patient_id
    if request.method == 'POST':
        form = HistoryForm(request.POST)
        if form.is_valid():
            update_history(form, history_pk, patient_id)
            messages.add_message(request, messages.SUCCESS, 'Successfully updated history')
            return HttpResponseRedirect(reverse('edit_history', args=[history_pk]))
        else:
            print(form.errors)
    else:
        form = HistoryForm()

    context = {
        'form': form,
        'patient_id': patient_id,
    }
    return render(request, 'Histories/historyUpdate.html', context)


