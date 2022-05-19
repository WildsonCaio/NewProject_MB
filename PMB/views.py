from django.shortcuts import render, redirect
from .models import Register_Employeers, Register_Services, Register_Time, Schedule

def agenda(request):
    employeers = Register_Employeers.objects.all()
    services = Register_Services.objects.all()
    time = Register_Time.objects.all()
    return render(request, 'pages/index.html', {'employeers':employeers, 'services':services, 'time':time})


#CORRIGIR BUG AMANHÃ
def add_employeer(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        image = request.FILES.get('image')
        created = Register_Employeers.objects.create(user_id=request.user.id, name=name, phone=phone, photo=image)
        created.save()
        return redirect('add_employeer', {'employeer':employeer})
        
        
    else:    
        employeer = Register_Employeers.objects.all()
        return render(request, 'pages/add_employeer.html',{'employeer':employeer})

def add_service(request):
    return render(request, 'pages/add_service.html')

def add_time(request):
    return render(request, 'pages/add_time.html')