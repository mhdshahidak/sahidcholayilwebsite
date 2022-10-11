from django import forms
from .models import Contact
from django.forms.widgets import Select, TextInput


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Name'}),
            'subject': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Subject'}),
            'location': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Location'}),
            'email': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Email'}),
            'number': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Phone Number'}),
            'whatsapp_number': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Whatsapp Number'}),
            'date': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Date'}),
            'time': Select(attrs={'class': 'required form-control select', 'placeholder': 'Time'}),
        }
