from django import forms
from django.core.exceptions import ValidationError
from .models import Reservation, Platform, Apartment

class ReservationsForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['start_date', 'end_date', 'num_guests','fname','lname','email','purpose','company','t_sum','commission','rech_num','link_reservation','guest_document','apartment','platform'] 
        widgets = {
            'start_date': forms.DateInput(attrs={'class': 'form-control my-5'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control my-5'}),
            'num_guests': forms.IntegerField(attrs={'class': 'form-control my-5'}),
            'fname': forms.CharField(attrs={'class': 'form-control mb-5'}),
            'lname': forms.CharField(attrs={'class': 'form-control mb-5'}),
            'company': forms.CharField(attrs={'class': 'form-control mb-5'}),
            'email': forms.EmailInput(attrs={'class': 'form-control mb-5'}),
            'purpose': forms.Select(attrs={'class': 'form-control mb-5'}),
            't_sum': forms.DecimalField(attrs={'class': 'form-control mb-5'}),
            'commission': forms.DecimalField(attrs={'class': 'form-control mb-5'}),
            'rech_num': forms.CharField(attrs={'class': 'form-control mb-5'}),
            'link_reservation': forms.URLInput(attrs={'class': 'form-control mb-5'}),
            'guest_document': forms.FileInput(attrs={'class': 'form-control mb-5'}),
            'apartment': forms.Select(attrs={'class': 'form-control mb-5'}),
            'platform': forms.Select(attrs={'class': 'form-control mb-5'}),

        }
        labels = {'start_date': 'check in', 'end_date': 'checkout', 'num_guests': 'number of guests', 'fname': 'first name', 'lname': 'last name', 'email': 'email', 'purpose': 'purpose', 'company': 'company', 't_sum': 'total sum', 'commission': 'commission', 'rech_num': 'rechnung number', 'link_reservation': 'link reservation', 'guest_document': 'guest document', 'apartment': 'apartment', 'platform': 'platform'}
    
    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     if 'django' in title:
    #         raise ValidationError('We do not accept notes about django ') 
    #     return title