from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request, 'main/home.html')

def doctor(request):
    return render(request, 'main/doctor.html')

def patient(request):
    return render(request, 'main/patient.html')
