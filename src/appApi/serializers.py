from rest_framework import serializers
from .models import *
from .serializers import *


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance
        fields = '__all__'


class AppoitmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appoitment
        fields = '__all__'

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'

class LaboratorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Laboratory
        fields = '__all__'

class DoctorTimeTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorTimeTable
        fields = '__all__'


        