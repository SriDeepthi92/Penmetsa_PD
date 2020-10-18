from django.shortcuts import render
from django.urls import include, path
from accounts import views
from django.contrib.auth import login
from django.views.generic.base import TemplateView
from clinic.models import TestSession
from django.shortcuts import render

def home(request):
    return render(request,'clinic/home.html')

def patient(request):
    return render(request,'clinic/patient.html')

def researcher(request):
    return render(request,'clinic/researcher.html')

def physician(request):
    return render(request,'clinic/physician.html')

def patient_data1(request):
    return render(request,'patient/patient_data1.html')

def patient_data2(request):
    return render(request,'patient/patient_data2.html')

def patient_data3(request):
    return render(request,'patient/patient_data3.html')

def patient_data4(request):
    return render(request,'patient/patient_data4.html')

def Test(request):
    Test_Session = TestSession.objects.all()
    return render(request, 'patient/list.html', locals())
