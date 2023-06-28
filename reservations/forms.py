from django import forms
from django.core.exceptions import ValidationError
from .models import Reservation, Platform, Apartment




class DateInput(forms.DateInput):
    input_type = 'date'
 
class ReservationsForm(forms.ModelForm):
    start_date = forms.DateField(widget=DateInput(attrs={'class': 'form-control my-5'}))
    end_date = forms.DateField(widget=DateInput(attrs={'class': 'form-control my-5'}))


    class Meta:
        model = Reservation
        fields = ['start_date', 'end_date', 'num_guests', 'fname', 'lname', 'email', 'purpose', 'company', 't_sum', 'commission', 'rech_num', 'link_reservation', 'guest_document', 'apartment', 'platform']
        widgets = {
            'end_date': forms.DateInput(attrs={'class': 'form-control my-5'}),
            'num_guests': forms.NumberInput(attrs={'class': 'form-control my-5'}),
            'fname': forms.TextInput(attrs={'class': 'form-control mb-5'}),
            'lname': forms.TextInput(attrs={'class': 'form-control mb-5'}),
            'company': forms.TextInput(attrs={'class': 'form-control mb-5'}),
            'email': forms.EmailInput(attrs={'class': 'form-control mb-5'}),
            'purpose': forms.Select(attrs={'class': 'form-control mb-5'}),
            't_sum': forms.NumberInput(attrs={'class': 'form-control mb-5'}),
            'commission': forms.NumberInput(attrs={'class': 'form-control mb-5'}),
            'rech_num': forms.TextInput(attrs={'class': 'form-control mb-5'}),
            'link_reservation': forms.URLInput(attrs={'class': 'form-control mb-5'}),
            'guest_document': forms.ClearableFileInput(attrs={'class': 'form-control mb-5'}),
            'apartment': forms.Select(attrs={'class': 'form-control mb-5'}),
            'platform': forms.Select(attrs={'class': 'form-control mb-5'}),
        }
        labels = {'start_date': 'Check-in', 'end_date': 'Checkout', 'num_guests': 'Number of Guests', 'fname': 'First Name', 'lname': 'Last Name', 'email': 'Email', 'purpose': 'Purpose', 'company': 'Company', 't_sum': 'Total Sum', 'commission': 'Commission', 'rech_num': 'Rechnung Number', 'link_reservation': 'Link Reservation', 'guest_document': 'Guest Document', 'apartment': 'Apartment', 'platform': 'Platform'}


class ApartmentForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = ['name','address','date_contract'] 
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'address': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'date_contract': forms.DateInput(attrs={'class': 'form-control my-5'}),
        }
        labels = {'name': 'Name', 'address': 'Address', 'date_contract': 'Date Contract'}


class Platformform(forms.ModelForm):
    class Meta:
        model = Platform
        fields = ['name','address','kundennummer','tel','login','url'] 
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'address': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'kundennummer': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'tel': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'login': forms.URLInput(attrs={'class': 'form-control my-5'}),
            'url': forms.URLInput(attrs={'class': 'form-control my-5'}),
        }
        labels = {'name': 'Name', 'address': 'Address', 'kundennummer': 'Kundenummer', 'tel': 'Telephone', 'login': 'Login', 'url': 'URL'}