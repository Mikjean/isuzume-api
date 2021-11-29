from django.db import models

# Create your models here.
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)

from django.db import models
from django.db.models.fields import CharField, GenericIPAddressField
from rest_framework_simplejwt.tokens import RefreshToken


class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError('Users should have a username')
        if email is None:
            raise TypeError('Users should have a Email')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None):
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


# AUTH_PROVIDERS = {'facebook': 'facebook', 'google': 'google',
#                   'twitter': 'twitter', 'email': 'email'}


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # auth_provider = models.CharField(
    #     max_length=255, blank=False,
    #     null=False, default=AUTH_PROVIDERS.get('email'))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }


# class Patient(models.Model):
#     user = models.ForeignKey(User)
#     patient_id = models.CharField(max_length=15, null=True)
#     first_name = models.CharField(max_length=40, null=True)
#     second_name = models.CharField(max_length=65, null=True)
#     date_of_birth = models.DateField()
#     gender = models.CharField(max_length=65)
#     phone_number = models.IntegerField()
#     address = models.IntegerField(max_length=60)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.first_name


# class Doctor(models.Model):
#     user = models.ForeignKey(User)
#     prefix = models.CharField()
#     specialist = models.Choices()
#     status = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.user

# class Insurance(models.Model):   
#     name = models.CharField(max_length=150)
#     address = models.CharField(max_length=500)
#     contacts = models.CharField(max_length=1000)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name


# class Laboratory(models.Model):   
#     name = models.CharField(max_length=150)
#     contacts = models.CharField(max_length=1000)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name


# class Hospital(models.Model):
#     laboratory = models.ForeignKey(Laboratory)   
#     name = models.CharField(max_length=150)
#     address = models.CharField(max_length=500)
#     contacts = models.CharField(max_length=1000)
#     description = models.TimeField()
#     district = models.Choices()
#     province = models.BooleanField(default=True)
#     is_public = models.BooleanField(default=True)
#     accepted_insurance = models.ForeignKey(Insurance)

#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name



# class DoctorTimeTable(models.Model):
#     doctor = models.ForeignKey(User)
#     hospital = models.ForeignKey(Hospital)
#     schedule_id = models.CharField()
#     schedule_date = models.Choices()
#     start_time = models.BooleanField(default=True)
#     end_time_time = models.BooleanField(default=True)
#     status = models.BooleanField(default=True)

#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.doctor

# class Appoitment(models.Model):
#     doctor = models.ForeignKey(Doctor)
#     patient = models.ForeignKey(Patient)
#     appoitment_id = models.CharField()
#     reason = models.CharField(max_length=500)
#     doctor_comment = models.CharField(max_length=1000)
#     appoitment_time = models.TimeField()
#     appoitment_date = models.Choices()
#     status = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.appoitment_id











