from django.shortcuts import render
from .models import Register_Employeers, Register_Services, Register_Time, Schedule

def index(request):
    employeers = Register_Employeers.objects.all()
    services = Register_Services.objects.all()
    time = Register_Time.objects.all()
    return render(request, 'pages/index.html', {'employeers':employeers, 'services':services, 'time':time})
