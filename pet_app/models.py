from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Login(AbstractUser):
    is_officer = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)
    name = models.CharField(max_length=25,null=True)
    phone_number = models.IntegerField(null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=50,null=True)
    address = models.TextField(null=True)
    qualification = models.CharField(max_length=50,null=True)
    status = models.BooleanField(default=0,null=True)


class PetRegister(models.Model):
    customer = models.ForeignKey(Login, on_delete=models.CASCADE,null=True)
    licence_no = models.CharField(max_length=25,null=True)
    # name = models.CharField(max_length=50)
    owner = models.CharField(max_length=20,null=True)
    pet_type = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    vaccinated = models.CharField(max_length=50)
    Description = models.TextField(null=True)
    status = models.IntegerField(default=0)
    expiry_date = models.DateField(null=True)

class Schedule(models.Model):
    customer = models.ForeignKey(Login, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

class Appointment(models.Model):
    userperson = models.ForeignKey(Login, on_delete=models.CASCADE,null=True)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)

class Complaint(models.Model):
    userperson = models.ForeignKey(Login, on_delete=models.DO_NOTHING)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField()
    reply = models.TextField(null=True, blank=True)
