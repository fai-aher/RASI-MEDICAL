from ..models import History

def get_history_by_patient_id(patient_pk):
    # Try to get the history for the given patient_pk
    history, created = History.objects.get_or_create(patient_id=patient_pk)

    # If created is True, it means a new history object was created
    if created:
        # You can initialize default values for the history object here
        history.state = 'New Patient'
        history.observation = ''
        history.save()

    return history

def get_history_by_id(history_pk):
    return History.objects.get(pk=history_pk)

def update_history(form, history_pk, patient_id):
    form.instance.pk = history_pk
    form.instance.patient_id = patient_id
    history = form.save()
    history.save()
    return history
