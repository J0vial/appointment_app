from multiprocessing import context
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from authentication.views import login_request
from main.models import doctor, hospital
from authentication.models import additionalUserInfo,User


# Create your views here.

def homepage(request):
    return render(request, 'main/home.html')

def Hospital_admin(request):
    query = additionalUserInfo.objects.filter(catagory ='Hospital-admin').values('status')
    #curr_user = User.objects.get(id = pk)

    return render(request, 'main/Hospital_admin.html',context = {'data':query,'adminpage':True})

def update_pat(request,pk):
    if request.method=='POST':
    
        fname= request.POST['fname']
        lname = request.POST['lname']
        email= request.POST['email']
        phone_no = request.POST['phone']
        
        user = User.objects.get(id = pk)
        add  = additionalUserInfo.objects.get(user_id = pk)
        user.first_name = fname
        user.last_name = lname
        user.email = email
        add.phone_no = phone_no
        
        
        user.save()
        add.save()
    return HttpResponseRedirect(reverse('main:patient'))
    
def edit_info_patient(request,pk):
    user = User.objects.get(id=pk)
    add  = additionalUserInfo.objects.get(user_id= pk)

    context = {
        'users': user,
        'addi':add
        
        
    }

    return render(request, 'main/edit_info_patient.html',context)
    
    

def patient(request):
    return render(request, 'main/patient.html')


def appoint(request):
    return render(request, 'main/appoint.html')



def hos_doc_list(request):
    query = doctor.objects.all()
    
    
    context = {'all_data':query}
    return render(request, 'main/hos_doc_list.html',context)

#--------------------------doctor-----------------------------------#
def register_doc(request):
    
    if request.method =='POST':
        name = request.POST.get('name')
        department = request.POST.get('department')
        hospital_name = request.POST.get('hospital')
        degree = request.POST.get('degree')
        date = request.POST.get('date')
        
        
            
        re_doc = doctor(name = name, depart = department,hos_name =hospital.objects.get(hos_name = hospital_name),date = date, degree=degree)
        re_doc.save()
    
    queryset = hospital.objects.all().order_by('hos_name')
    dpt = ['Allergists',
           'Dermatologists',
           'Ophthalmologists',
           'gynecologists',
           'Cardiologists'                   
        ]   
    return render(request, 'main/regi_doc.html',context={'models':queryset,'department':dpt})

def edit_doc(request):
    
    query = doctor.objects.all()
    
    
    context = {'all_data':query}
    return render(request, 'main/edit_doc_info.html',context)

def deleteDoc(request,pk):
    doc = doctor.objects.get(id=pk)
    doc.delete()
    return HttpResponseRedirect(reverse('main:edit_doc_info'))

def updateDoc(request,pk):
    
    mymember = doctor.objects.get(id=pk)
    
    queryset = hospital.objects.all().order_by('hos_name')
    dpt = ['Allergists',
           'Dermatologists',
           'Ophthalmologists',
           'gynecologists',
           'Cardiologists'                   
        ]   
    context = {
        'mymember': mymember,
        'models':queryset,
        'department':dpt
        
    }
    
    return render(request, 'main/update.html',context)
def updaterecord(request, pk):
    if request.method =="POST":
    
        name= request.POST['name']
        department = request.POST['department']
        hospital_name = request.POST['hospital']
        degree = request.POST['degree']
        date = request.POST['date']
            
    
        member = doctor.objects.get(id=pk)
        member.name = name
        member.depart = department
        member.degree = degree
        member.hos_name = hospital.objects.get(hos_name = hospital_name)
        member.date = date
    
        member.save()
    return HttpResponseRedirect(reverse('main:edit_doc_info'))
    


    

