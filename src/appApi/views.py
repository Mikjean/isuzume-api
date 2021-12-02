from django.shortcuts import render
import rest_framework
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from .serializers import *
from rest_framework import permissions
from .permissions import IsDoctor, IsOwner
from rest_framework import permissions

# Create your views here.
class DoctorListView(ListCreateAPIView):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
    permission = [permissions.IsAuthenticatedOrReadOnly]


class DoctorDetailView(RetrieveUpdateAPIView):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
    permission = [permissions.AllowAny]

    lookup_field = "id"
    

class PatientListView(ListCreateAPIView):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()
    permission = [permissions.IsAuthenticated]


class PatientDetailView(RetrieveUpdateAPIView):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()
    lookup_field = "id"
    permission = [permissions.IsAuthenticated]


class InsuranceListView(ListCreateAPIView):
    serializer_class = InsuranceSerializer
    queryset = Insurance.objects.all()
    permission = [permissions.IsAuthenticatedOrReadOnly]

class InsuranceDetailView(RetrieveUpdateAPIView):
    serializer_class = InsuranceSerializer
    queryset = Insurance.objects.all()
    lookup_field = "id"
    permission = [permissions.IsAuthenticated]

class AppoitmentListView(ListCreateAPIView):
    serializer_class = AppoitmentSerializer
    queryset = Appoitment.objects.all()
    permission = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(user = self.request.user)

    # def get_queryset(self):
    #     return self.queryset.filter(doctor=self.request.user)

class AppoitmentDetailView(RetrieveUpdateAPIView):
    serializer_class = AppoitmentSerializer
    queryset = Appoitment.objects.all()
    lookup_field = "id"
    permission = [permissions.IsAuthenticated| IsOwner | IsDoctor]
    
    def get_queryset(self):
        return self.queryset.filter(doctor=self.request.user) | self.queryset.filter(user=self.request.user)
        

class HospitalListView(ListCreateAPIView):
    serializer_class = HospitalSerializer
    queryset = Appoitment.objects.all()
    permission = [permissions.IsAuthenticatedOrReadOnly | permissions.IsAdminUser | IsDoctor]


class HospitalDetailView(RetrieveUpdateAPIView):
    serializer_class = HospitalSerializer
    queryset = Hospital.objects.all()
    lookup_field = "id"
    permission = [permissions.IsAuthenticatedOrReadOnly]


class LaboratoryListView(ListCreateAPIView):
    serializer_class = LaboratorySerializer
    queryset = Laboratory.objects.all()
    permission = [permissions.IsAuthenticated]

class LaboratoryDetailView(RetrieveUpdateAPIView):
    serializer_class = LaboratorySerializer
    queryset = Laboratory.objects.all()
    lookup_field = "id"
    permission = [permissions.IsAuthenticated]


class DoctorTimeTableListView(ListCreateAPIView):
    serializer_class = DoctorTimeTableSerializer
    queryset = DoctorTimeTable.objects.all()
    permission = [permissions.AllowAny | IsOwner | IsDoctor]

    def get_queryset(self):
        return self.queryset.filter(doctor=self.request.user)

class DoctorTimeTableDetailView(RetrieveUpdateAPIView):
    serializer_class = DoctorTimeTableSerializer
    queryset = DoctorTimeTable.objects.all()
    lookup_field = "id"
    permission = [permissions.IsAuthenticatedOrReadOnly, permissions.IsAdminUser]

    def get_queryset(self):
        return self.queryset.filter(doctor=self.request.user)



