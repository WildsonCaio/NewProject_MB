from itertools import product
from unicodedata import name
from django.shortcuts import render, redirect
from .models import Register_Employeers, Register_Services, Register_Time, Schedule


def agenda(request):
    employeers = Register_Employeers.objects.all()
    services = Register_Services.objects.all()
    time = Register_Time.objects.all()
    return render(request, 'pages/index.html', {'employeers':employeers, 'services':services, 'time':time})

def add_employeer(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        image = request.FILES.get('image')
        created = Register_Employeers.objects.create(user_id=request.user.id, name=name, phone=phone, photo=image)
        created.save()
        return redirect('add_employeer')
        
        
    else:    
        employeer = Register_Employeers.objects.all()
        return render(request, 'pages/add_employeer.html',{'employeer':employeer})

def add_service(request): 
    if request.method == "POST":
        employeers = Register_Employeers.objects.all()
        name = request.POST.get('name')
        technique = request.POST.get('technique')
        products = request.POST.get('product')
        professionals = request.POST.getlist('professionals')
        
        add = Register_Services(user_id=request.user.id, name=name, technique=technique, products=products)
        add.save()
        
        for i in professionals:
            a1 = Register_Employeers.objects.get(name=i)
            add.professionals.add(a1)
        
        
        return redirect('add_service')
    else:
        employeers = Register_Employeers.objects.all()
        return render(request, 'pages/add_services.html', {'employeers':employeers})

def add_time(request):
    return render(request, 'pages/add_time.html')