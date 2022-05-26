from django.shortcuts import render, redirect
from django.contrib import auth

def login_company(request):
    if request.method == 'POST':
        cnpj = request.POST.get('cnpj')
        password = request.POST.get('password')
        check_user = auth.authenticate(request, username=cnpj, password=password)
        if check_user is not None and check_user.is_superuser:
            return redirect('agenda')
        else:
            return render(request, 'pages/login_company.html')

    else:    
        return render(request, 'pages/login_company.html')
