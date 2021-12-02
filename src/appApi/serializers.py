from rest_framework import serializers
from .models import *
from .serializers import *



class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'

        
class DoctorSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    url = serializers.HyperlinkedIdentityField(view_name='doctor-detail',lookup_field = 'id')
    class Meta:
        model = Doctor
        fields = ['id','prefix','user','url','description','specialist', 'status']
    
    def get_user(self, obj):
        return str(obj.user.username)

class DoctorDetailSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    hospital = serializers.SerializerMethodField()

    class Meta:
        model = Doctor
        fields = ['id','prefix','user','description','specialist', 'status', 'hospital']

    def get_user(self, obj):
        return str(obj.user.username)

    def get_hospital(self,obj):
        return HospitalSerializer(obj.hospital_set.all(),many=True).data

    


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



class LaboratorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Laboratory
        fields = '__all__'

class DoctorTimeTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorTimeTable
        fields = '__all__'


        