from django.urls import path 
from . import views 

urlpatterns = [ 
    path('entrar/', views.login_company, name='login_company')
]