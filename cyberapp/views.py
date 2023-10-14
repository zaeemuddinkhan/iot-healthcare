from typing import Any, Dict
from django.shortcuts import render,get_object_or_404
from cyberapp.models import Appointment

from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import render

def index(request):
    return render(request, 'cyberapp/index.html')

def about(request):
    return render(request, 'cyberapp/about.html')

def service(request):
    return render(request, 'cyberapp/service.html')

def doctor(request):
    return render(request, 'cyberapp/doctor.html')

def contact(request):
    return render(request, 'cyberapp/contact.html')

from django.shortcuts import render, redirect
from .forms import AppointmentForm

from django.shortcuts import render, redirect
from .forms import AppointmentForm

def make_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            make_appointment = Appointment(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                mobile_no=form.cleaned_data['mobile_no'],
                sex=form.cleaned_data['sex'],
                appointment_date=form.cleaned_data['appointment_date'],
                message=form.cleaned_data['message'],      
            )
            form.save()
            return HttpResponseRedirect('/service')  # Replace 'success_page' with your success page URL
    else:
        form = AppointmentForm()

    return render(request, 'cyberapp/form.html', {'form': form})


def appointment(request):
    if request.method == 'POST':
        entered_first_name = request.POST['first_name']
        print(entered_first_name)
        return HttpResponseRedirect("/form")
    return render(request, "cyberapp/index.html")

def form(request):
    return render(request, "cyberapp/form.html")