from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('doctors/', DoctorListView.as_view(), name="all-doctors"),
    path('doctor/<str:id>', DoctorDetailView.as_view(), name="doctor-detail"),
    path('patients/', PatientListView.as_view(), name="all-patients"),
    path('patient/<str:id>', PatientDetailView.as_view(), name="patient-detail"),
    path('insurances/', InsuranceListView.as_view(), name="all-insurances"),
    path('insurance/<str:id>', InsuranceDetailView.as_view(), name="insurance-detail"),
    path('appoitments/', AppoitmentListView.as_view(), name="all-appoitments"),
    path('appoitment/<str:id>', AppoitmentDetailView.as_view(), name="appoitment-detail"),
    path('hospitals/', HospitalListView.as_view(), name="all-hospitals"),
    path('hospital/<str:id>', HospitalDetailView.as_view(), name="hospital-detail"),
    path('labolatories/', HospitalListView.as_view(), name="all-hospitals"),
    path('labolator/<str:id>', HospitalDetailView.as_view(), name="hospital-detail"),    
    
]