from django.db import models
from isuzumeApi.models import User


class Insurance(models.Model):   
    name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    insurance = models.ForeignKey(Insurance, on_delete=models.CASCADE)
    patient_id = models.CharField(max_length=15, null=True)    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user


class Doctor(models.Model):

    SPECIALITIES = [
        ('genecologist', 'genecologist'),
        ('pediatrician', 'pediatrician'),
        ('ophtamologist', 'ophtamologist'),
        ('generalist', 'generalist')
        ]


    PREFIXES = [
        ('Dr', 'Doctor'),
        ('PTA', 'Pediatrician'),
        ('PSo', 'Psycologist'),
        ('Gdr', 'generalist')
        ]
        
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    prefix = models.CharField(max_length=15, choices=PREFIXES, default=None)
    description = models.TextField(max_length=500)
    specialist = models.CharField(max_length=40, choices=SPECIALITIES)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user


class Laboratory(models.Model):   
    name = models.CharField(max_length=150)
    contacts = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Hospital(models.Model):

    PROVINCES = [
        ('North', 'Doctor'),
        ('East', 'East'),
        ('West', 'West'),
        ('South', 'South')
        ]
    laboratory = models.ForeignKey(Laboratory, on_delete=models.CASCADE)   
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=500)
    district = models.CharField(max_length=50)
    province = models.CharField(max_length=55, choices=PROVINCES)
    is_public = models.BooleanField(default=True)
    accepted_insurance = models.ForeignKey(Insurance, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class DoctorTimeTable(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete= models.CASCADE)
    schedule_id = models.CharField(max_length=15)
    schedule_date = models.DateField()
    start_time = models.DateTimeField()
    end_time = models.TimeField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.doctor

class Appoitment(models.Model):

    APPOITMENT_STATUS = [
        ('booked', 'booked'),
        ('pending', 'pending'),
        ('approved', 'approved'),
        ('completed', 'completed')
        ]

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appoitment_id = models.CharField(max_length=15)
    reason = models.CharField(max_length=500)
    doctor_comment = models.CharField(max_length=1000)
    lab_comments = models.CharField(max_length=1000)
    appoitment_time = models.DateField()
    status = models.CharField(choices=APPOITMENT_STATUS,max_length=25,default='booked')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.appoitment_id

