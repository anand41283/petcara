import django_filters
from django import forms
from django_filters import CharFilter

from pet_app.models import PetRegister


class PetRegisterFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', label="", lookup_expr='icontains', widget=forms.TextInput(attrs={
        'placeholder': 'Search Name', 'class': 'form-control'}))

    class Meta:
        model = PetRegister
        fields = ('name',)
