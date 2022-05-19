from django.urls import path 
from . import views 

urlpatterns=[
    path('agendar/', views.agenda, name='agenda'),
    path('adicionar_funcionarios/', views.add_employeer, name='add_employeer'),
    path('adicionar_servicos/', views.add_service, name='add_service'),
    path('adicionar_horarios/', views.add_time, name='add_time'),
]