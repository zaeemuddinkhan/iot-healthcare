from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
       
        fields = ['first_name', 'last_name', 'email', 'mobile_no', 'sex', 'appointment_date', 'message']
