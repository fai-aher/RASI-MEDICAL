from rest_framework import serializers
from histories.models import History, HistoryEdit, Prescription, LabResult

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'

class HistoryEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryEdit
        fields = '__all__'

class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = '__all__'

class LabResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabResult
        fields = '__all__'