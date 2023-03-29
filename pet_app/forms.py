import re

from crispy_forms.layout import Layout, Row, Column
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from pet_app.models import Login, PetRegister,Schedule,Complaint


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'

def phone_number_validator(value):
    if not re.compile(r'^[7-9]\d{9}$').match(value):
        raise ValidationError('This is Not a Valid Phone Number')


class OfficerRegister(UserCreationForm):
    phone_number = forms.CharField(validators=[phone_number_validator])
    email = forms.CharField(validators=[
        RegexValidator(regex='^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', message='Please Enter a Valid Email')])
    class Meta:
        model = Login
        fields = ('username','name','email','phone_number','password1', 'password2','qualification','address')

class OfficerUpdateForm(UserCreationForm):
    phone_number = forms.CharField(validators=[phone_number_validator])
    email = forms.CharField(validators=[
        RegexValidator(regex='^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', message='Please Enter a Valid Email')])

    class Meta:
        model = Login
        fields = ('username','name','email','phone_number','password1', 'password2','qualification','address')


gender_choice = (
    ("Male", "Male"),
    ("Female", "Female"),
)


class CustomerRegister(UserCreationForm):
    phone_number = forms.CharField(validators=[phone_number_validator])
    gender = forms.ChoiceField(choices=gender_choice, required=True, widget=forms.RadioSelect)
    email = forms.CharField(validators=[
        RegexValidator(regex='^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', message='Please Enter a Valid Email')])
    class Meta:
        model = Login
        fields = ('username','name','email','phone_number','age','gender','address','password1', 'password2')



Vaccine_CHOICES = (
    ('Yes', 'Yes'),
    ('No', 'No'),
)


class PetRegisterForm(forms.ModelForm):
    vaccinated = forms.ChoiceField(widget=forms.RadioSelect, choices=Vaccine_CHOICES)
    expiry_date = forms.DateField(widget=DateInput)

    class Meta:
        model = PetRegister
        fields = ('owner','licence_no','expiry_date','pet_type', 'breed','Description', 'vaccinated')

class SchdeuleForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    start_time = forms.TimeField(widget=TimeInput, )
    end_time = forms.TimeField(widget=TimeInput, )

    class Meta:
        model = Schedule
        fields = ('date', 'start_time', 'end_time')

class ComplaintForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)

    class Meta:
        model = Complaint
        fields = ('subject', 'content', 'date')