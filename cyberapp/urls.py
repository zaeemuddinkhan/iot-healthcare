from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('doctor/', views.doctor, name='doctor'),
    path('contact/', views.contact, name='contact'),
    path('make-appointment/', views.make_appointment, name='make_appointment'),
    path('form/', views.form, name='form')
]

