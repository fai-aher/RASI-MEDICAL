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
    if request.method == 'POST':
        form = HistoryForm(request.POST, instance=history)
        if form.is_valid():
            form.save()
            # Creacion de una nueva instancia de HistoryEdit
            HistoryEdit.objects.create(
                history=history,
                patient_id=history.patient_id,
                state=history.state,
                observations=history.observations,
                date_of_birth=history.date_of_birth,
                blood_type=history.blood_type,
                allergies=history.allergies,
                medications=history.medications,
                past_diseases=history.past_diseases,
                surgeries=history.surgeries,
                family_history=history.family_history,
            )
            messages.add_message(request, messages.SUCCESS, 'Successfully updated history')
            return HttpResponseRedirect(reverse('edit_history', args=[history_pk]))
        else:
            print(form.errors)
    else:
        form = HistoryForm(instance=history)

    context = {
        'form': form,
        'patient_id': history.patient_id,
    }
    return render(request, 'Histories/historyUpdate.html', context)


