#logic of the patients app

from ..models import Patient

def get_patients():
    patients = Patient.objects.all()
    return patients

#Methods to get by ID

def get_patient_by_id(patient_pk):
    patient = Patient.objects.get(pk=patient_pk)
    return patient

# Method to POST a patient
def post_patient(patient):
    patient = Patient.objects.create(**patient)
    return patient

# Method to PUT (Update) a patient
def update_patient(patient_pk, new_patient):
    patient = get_patient_by_id(patient_pk)
    #Assigning the new values
    patient.name = new_patient['name']
    patient.save()
    return patient


def create_patient(serializer):
    patient = serializer.save()
    return patient
